from src.users.dtos import UserSchema
from src.users.models import UserModel
from fastapi import HTTPException
from sqlalchemy.orm import Session
from src.users.security_config import get_password


def register(body: UserSchema, db: Session):
    """
        we will check if the username and email are individually unique 
        then only we will create/ register the user 
    """
    
    # ".first() returns the first matching record and None if username is not found"
    is_user_username = db.query(UserModel).filter(UserModel.username == body.username).first()
    is_user_email = db.query(UserModel).filter(UserModel.email == body.email).first()
    
    if is_user_username:
        raise HTTPException(400, detail="Username already exists...")
    if is_user_email:
        raise HTTPException(400, detail="email already exists...")
    
    hash_password = get_password(body.password)
    # print(hash_password)
    
    data = body.model_dump()
    new_user: UserModel = UserModel()
    new_user.name = data['name']
    new_user.username = data['username']
    new_user.email = data['email']
    new_user.hash_password = hash_password
    
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    
    return new_user