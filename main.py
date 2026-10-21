from fastapi import FastAPI
from src.utils.db import Base, engine
from src.tasks.router import task_routes
from src.tasks.models import TaskModel
from src.users.router import user_routes

# as soon as our server starts it connects to db
Base.metadata.create_all(engine) 

app = FastAPI(title="Task Management App")
app.include_router(task_routes)
app.include_router(user_routes)