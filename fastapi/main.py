# from fastapi import FastAPI

# app = FastAPI()

# @app.get("/get")
# def home():
#     return {"message": "working"}


 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
 
app = FastAPI()

todos = []

class Todo(BaseModel):
    title: str
    completed: bool = False


@app.get("/")
def home():
    return {"message": "FastAPI working"}

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    print(todos)
    return todo

@app.get("/todos/{todo_id}")
def get_todo(todo_id: int):
    if todo_id < 0 or todo_id >= len(todos):

        raise HTTPException(
            status = 404,
            detail ="Todo not found"
        )
    
    return todos[todo_id]
