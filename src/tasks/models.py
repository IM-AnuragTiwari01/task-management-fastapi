from sqlalchemy import Column, String, Boolean, Text
from src.utils.db import Base
import uuid
from sqlalchemy.dialects.mysql import CHAR

class TaskModel(Base):
    __tablename__ = "user_tasks"
    
    id = Column(
        CHAR(36), 
        primary_key=True, 
        default=lambda: str(uuid.uuid4())
    )
    title = Column(String(255), nullable=False)
    description = Column(Text, nullable=True)
    is_completed = Column(Boolean, default=False)