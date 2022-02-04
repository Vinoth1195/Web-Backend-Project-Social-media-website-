from datetime import date, datetime
from lib2to3.pgen2.token import OP
from sqlite3 import Timestamp
from time import timezone

from typing import Optional
from xmlrpc.client import DateTime
from markupsafe import string
from pydantic import BaseModel, EmailStr, conint


class Users(BaseModel):
    email: EmailStr
    password:str

class UserCreated(BaseModel):
    id: int
    email: EmailStr
    timestamp: datetime
    

    class Config:
        orm_mode = True


class Posts(BaseModel):
    title:str
    content:Optional[str]
    published: bool = True

class ReturnPosts(Posts):
    id: int
    timestamp: datetime
    owner_id: int
    owner: UserCreated
    class Config:
        orm_mode = True

class ReturnAllPosts(BaseModel):
    Posts2: ReturnPosts
    votes: int

    class Config:
        orm_mode = True

class Token(BaseModel):
    Email: EmailStr
    Password: str

class TokenData(BaseModel):
    id: Optional[str] = None
    expires: Optional[datetime]


class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)