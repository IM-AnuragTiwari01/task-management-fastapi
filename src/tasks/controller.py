from src.tasks.models import TaskModel
from sqlalchemy.orm import Session
from src.tasks.dtos import TaskSchema
from fastapi import HTTPException
from uuid import UUID

def create_task(body: TaskSchema, db:Session):
    data = body.model_dump()
    new_task: TaskModel = TaskModel(**data)
    
    # another way non-pythonic way
    # new_task.title = data['title']
    # new_task.description = data['description']
    # new_task.is_completed = data['is_completed']
    
    
    db.add(new_task)
    db.commit()
    db.refresh(new_task) 
    
    return {
        "status": "Created Data Successfully",
        "response": new_task
    }
    
def get_tasks(db: Session):
    tasks = db.query(TaskModel).all()
    
    return {
        "status": "All Tasks",
        "response": tasks
    }
    
def get_task_by_id(db: Session, task_id: UUID):
    task = db.query(TaskModel).get(task_id)
    
    if not task:
        raise HTTPException(404, detail=f"Task : id:{task_id} not found!")
    
    return {
        "status": f"Task : id:={task_id} found!",
        "response": task
    }
    
def update_task(body: TaskSchema, task_id: int, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail=f"Task : id:{task_id} not found!")
    body = body.model_dump(exclude_unset=True)
    
    for field, value in body.items():
        setattr(task, field, value)
        
    db.add(task)
    db.commit()
    db.refresh(task)
    
    return {
        "status": f"Updated Task with id: {task_id}",
        "response": task
    }
    
def delete_task(task_id: UUID, db: Session):
    task = db.query(TaskModel).get(task_id)
    if not task:
        raise HTTPException(404, detail=f"Task : id:{task_id} not found!")
    
    db.delete(task)
    db.commit()
    return {
        "status": "Task Deleted",
        "response": task
    }
    