from fastapi import FastAPI
from app.db.database import Base, engine

from app.models import user, job
from app.routers import auth, job as job_router

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Job System with JWT Auth")

app.include_router(auth.router)
app.include_router(job_router.router)


@app.get("/")
def root():
    return {"message": "System running"}