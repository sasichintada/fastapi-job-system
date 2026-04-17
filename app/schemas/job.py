from pydantic import BaseModel
from typing import Optional


class JobCreate(BaseModel):
    task_name: str


class JobResponse(BaseModel):
    id: int
    status: str
    result: Optional[str] = None

    class Config:
        from_attributes = True