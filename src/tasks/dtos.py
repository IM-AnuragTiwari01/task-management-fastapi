from pydantic import BaseModel
from typing import Optional

class TaskSchema(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    is_completed: Optional[bool] = False