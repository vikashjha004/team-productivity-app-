from fastapi import APIRouter
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import Task

router = APIRouter(prefix="/tasks")

@router.post("/")
def create_task(name: str, assigned_to: int):
    db: Session = SessionLocal()
    task = Task(name=name, assigned_to=assigned_to)
    db.add(task)
    db.commit()
    return task

@router.get("/my/{user_id}")
def my_tasks(user_id: int):
    db: Session = SessionLocal()
    return db.query(Task).filter(Task.assigned_to == user_id).all()
