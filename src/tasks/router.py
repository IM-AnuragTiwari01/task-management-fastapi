from fastapi import APIRouter, Depends
from src.tasks.dtos import TaskSchema
from src.tasks import controller
from src.utils.db import get_db
from sqlalchemy.orm import Session
from uuid import UUID

task_routes = APIRouter(prefix="/tasks")

@task_routes.post("/create-task")
def create_task(body: TaskSchema, db:Session = Depends(get_db)):
    return controller.create_task(body, db)

@task_routes.get("/get-all-tasks")
def get_tasks(db: Session = Depends(get_db)):
    return controller.get_tasks(db)

@task_routes.get("/get-task/{task_id}")
def get_task_by_id(task_id: UUID, db: Session = Depends(get_db)):
    return controller.get_task_by_id(db, task_id)

@task_routes.put("/update-task/{task_id}")
def update_task(body: TaskSchema, task_id: UUID, db:Session = Depends(get_db)):
    return controller.update_task(body, task_id, db)

@task_routes.delete("/delete-task/{task_id}")
def delete_task(task_id: UUID, db:Session = Depends(get_db)):
    return controller.delete_task(task_id, db)