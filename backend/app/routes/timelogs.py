from fastapi import APIRouter
from datetime import datetime
from sqlalchemy.orm import Session
from ..database import SessionLocal
from ..models import TimeLog

router = APIRouter(prefix="/timelog")

@router.post("/start")
def start(task_id: int, user_id: int, type: str):
    db: Session = SessionLocal()
    log = TimeLog(task_id=task_id, user_id=user_id, type=type)
    db.add(log)
    db.commit()
    return log

@router.post("/stop/{log_id}")
def stop(log_id: int):
    db: Session = SessionLocal()
    log = db.query(TimeLog).get(log_id)
    log.end_time = datetime.utcnow()
    db.commit()
    return log
