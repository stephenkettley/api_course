import time
from random import randrange
from typing import List, Optional

import psycopg2
from fastapi import Depends, FastAPI, HTTPException, Response, status
from psycopg2.extras import RealDictCursor
from pydantic import BaseModel
from sqlalchemy.orm import Session

from .entrypoints import post, user
from .entrypoints.schemas import models, schemas, utils
from .entrypoints.schemas.database import engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


while True:
    try:
        conn = psycopg2.connect(
            host="localhost",
            dbname="Social Media FastAPI Course",
            user="postgres",
            password="bornfreebeing",
            cursor_factory=RealDictCursor,
        )
        cursor = conn.cursor()
        print("database connection successful")
        break
    except Exception as error:
        print("database connection failed")
        print("error: ", error)
        time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)


@app.get("/")
def first_message():
    return {"message": "welcome to my api"}
