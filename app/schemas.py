from datetime import datetime

from pydantic import BaseModel, EmailStr


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # this creates a default value of True


class PostCreate(PostBase):
    pass


class ResponsePost(PostBase):
    id: int

    class Config:
        orm_mode = True


class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserOut(BaseModel):
    email: EmailStr
    id: int

    class Config:
        orm_mode = True
