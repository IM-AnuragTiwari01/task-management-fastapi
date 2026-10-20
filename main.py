from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.tasks.models import TaskModel

# as soon as our server starts it connects to db
Base.metadata.create_all(engine) 

app = FastAPI(title="Task Management App")
app.include_router(task_routes)