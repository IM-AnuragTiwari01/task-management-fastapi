from pydantic import BaseModel
from typing import Optional

class UserSchema(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    email: Optional[str] = None
    password: Optional[str] = None
    
class UserResponseSchema(BaseModel):
    username: Optional[str] = None
    email: Optional[str] = None
    hash_password: Optional[str] = None