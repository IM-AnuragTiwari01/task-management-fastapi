from sqlalchemy import Column, String, Boolean, Text
from src.utils.db import Base
import uuid
from sqlalchemy.dialects.mysql import CHAR

class UserModel(Base):
    __tablename__ = "user_table"
    
    id = Column(
        CHAR(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )
    name = Column(String(255))
    username = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    hash_password = Column(String(255), nullable=False)