from random import randrange
from typing import Optional

from fastapi import FastAPI, HTTPException, Response, status
from fastapi.params import Body
from pydantic import BaseModel

app = FastAPI()


class Post(BaseModel):
    title: str
    content: str
    published: bool = True  # this creates a default value of True
    rating: Optional[int] = None  # optional field that defaults to None


my_posts = [
    {"title": "title of post1", "content": "content of post1", "id": 1},
    {"title": "favourite foods", "content": "I like pizza", "id": 2},
]


def find_post(id):
    for p in my_posts:
        if p["id"] == id:
            return p


def find_index_post(id):
    for i, p in enumerate(my_posts):
        if p["id"] == id:
            return i


@app.get("/")
def first_message():
    return {"message": "welcome to my api"}


@app.get("/posts")
def get_posts():
    return {"data": my_posts}


@app.post("/posts", status_code=status.HTTP_201_CREATED)
def create_posts(post: Post):
    post_dict = post.dict()
    post_dict["id"] = randrange(0, 1000000)
    my_posts.append(post_dict)
    return {"data": post_dict}


@app.get("/posts/{id}")
def get_post(id: int):
    post = find_post(id)
    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} was not found",
        )
    return {"data": post}


@app.delete("/posts/{id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id: int):
    index = find_index_post(id)

    if index == None:
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"post with id {id} doest not exist",
        )
    my_posts.pop(index)
    return Response(status_code=status.HTTP_204_NO_CONTENT)
