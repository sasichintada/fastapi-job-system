from sqlalchemy import Column, Integer, String, Text
from app.db.database import Base


class Job(Base):
    __tablename__ = "jobs"

    id = Column(Integer, primary_key=True, index=True)
    status = Column(String, default="pending")
    result = Column(Text, nullable=True)