# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/get")
# def home():
#     return {"message": "working"}

from fastapi import FastAPI
from pydantic import BaseModel
 
app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "FastAPI working"}

@app.post("/todo")
def create_todo(todo:Todo):
    todos.append(todo)
    return todo

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    return todos[todo_id]