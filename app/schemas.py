from pydantic import BaseModel


class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True  # this creates a default value of True


class PostCreate(PostBase):
    pass
