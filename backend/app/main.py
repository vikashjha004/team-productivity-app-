from fastapi import FastAPI
from .database import Base, engine
from .routes import tasks, timelogs, reports

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Team Productivity App")

app.include_router(tasks.router)
app.include_router(timelogs.router)
app.include_router(reports.router)
