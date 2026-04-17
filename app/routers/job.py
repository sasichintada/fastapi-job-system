from fastapi import APIRouter, BackgroundTasks, Depends, HTTPException
from sqlalchemy.orm import Session
import time
import random

from app.db.database import get_db
from app.models.job import Job
from app.schemas.job import JobCreate, JobResponse
from app.core.deps import get_current_user


router = APIRouter(prefix="/jobs", tags=["Jobs"])


def process_job(job_id: int):
    db = next(get_db())

    job = db.query(Job).filter(Job.id == job_id).first()
    if not job:
        return

    try:
        job.status = "in_progress"
        db.commit()

        time.sleep(random.randint(5, 10))

        job.status = "completed"
        job.result = f"Job {job.id} completed successfully"
        db.commit()

    except Exception as e:
        job.status = "failed"
        job.result = str(e)
        db.commit()

    finally:
        db.close()


@router.post("/", response_model=JobResponse)
def create_job(
    job: JobCreate,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    new_job = Job(status="pending")
    db.add(new_job)
    db.commit()
    db.refresh(new_job)

    background_tasks.add_task(process_job, new_job.id)

    return new_job


@router.get("/{job_id}", response_model=JobResponse)
def get_job(
    job_id: int,
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    job = db.query(Job).filter(Job.id == job_id).first()

    if not job:
        raise HTTPException(status_code=404, detail="Job not found")

    return job


@router.get("/", response_model=list[JobResponse])
def get_all_jobs(
    db: Session = Depends(get_db),
    user: str = Depends(get_current_user)
):
    return db.query(Job).all()