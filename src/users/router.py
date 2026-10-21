from fastapi import APIRouter, Depends
from src.users.dtos import UserSchema, UserResponseSchema
from src.utils.db import get_db
from sqlalchemy.orm import Session
from src.users import controller
from uuid import UUID

user_routes = APIRouter(prefix="/users")

@user_routes.post("/register-user", response_model=UserResponseSchema)
def register(body:UserSchema, db: Session = Depends(get_db)):
    return controller.register(body, db)