from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

class UserReturn(BaseModel):
    username: str
    # id: str
    # email: EmailStr
    # created_at: datetime
    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str

class PostCreate(PostBase):
    pass

class PostReturn(PostBase):
    id: str
    created_at: datetime
    owner_id: int
    owner: UserReturn

    class Config:
        orm_mode = True


class PostVote(BaseModel):
    Post: PostReturn
    votes: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str
    username: str



class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Optional[str] = None

class OwnerReturn(BaseModel):
    name: str

class Vote(BaseModel):
    post_id: int
    vote_dir: int
    
    