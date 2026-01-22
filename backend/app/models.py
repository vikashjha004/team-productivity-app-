from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from .database import Base

class Task(Base):
    __tablename__ = "tasks"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    assigned_to = Column(Integer)
    status = Column(String, default="pending")

class TimeLog(Base):
    __tablename__ = "timelogs"
    id = Column(Integer, primary_key=True)
    task_id = Column(Integer)
    user_id = Column(Integer)
    start_time = Column(DateTime, default=datetime.utcnow)
    end_time = Column(DateTime, nullable=True)
    type = Column(String)
