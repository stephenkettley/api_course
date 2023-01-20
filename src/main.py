from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def first_message():
    return {"message": "welcome to my api"}
