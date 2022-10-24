from pydantic import BaseModel, EmailStr
from datetime import datetime

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class PostCreate(PostBase):
    pass

class PostReturn(PostBase):
    id: str
    created_at: datetime
    class Config:
        orm_mode = True

class UserCreate(BaseModel):
    email: EmailStr
    password: str

class UserReturn(BaseModel):
    id: str
    email: EmailStr
    created_at: datetime
    class Config:
        orm_mode = True