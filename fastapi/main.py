# # from fastapi import FastAPI

# # app = FastAPI()

# # @app.get("/get")
# # def home():
# #     return {"message": "working"}


 
# from fastapi import FastAPI, HTTPException
# from pydantic import BaseModel
 
# app = FastAPI()

# todos = []

# class Todo(BaseModel):
#     title: str
#     completed: bool = False


# @app.get("/")
# def home():
#     return {"message": "FastAPI working"}

# @app.post("/todos")
# def create_todo(todo:Todo):
#     todos.append(todo)
#     print(todos)
#     return todo

# @app.get("/todos/{todo_id}")
# def get_todo(todo_id: int):
#     if todo_id < 0 or todo_id >= len(todos):

#         raise HTTPException(
#             status = 404,
#             detail ="Todo not found"
#         )
    
#     return todos[todo_id]

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from database import SessionLocal, engine
from models import Base, Todo
from schemas import TodoCreate

app = FastAPI()

Base.metadata.create_all(bind=engine)


def get_db():

    db = SessionLocal()

    try:
        yield db

    finally:
        db.close()


@app.get("/get")
def home():
    return {"message": "FastAPI PostgreSQL working"}


@app.post("/todos")
def create_todo(
    todo: TodoCreate,
    db: Session = Depends(get_db)
):

    new_todo = Todo(
        title=todo.title,
        completed=todo.completed
    )

    db.add(new_todo)

    db.commit()

    db.refresh(new_todo)

    return new_todo


@app.get("/todos")
def get_todos(
    db: Session = Depends(get_db)
):

    todos = db.query(Todo).all()

    return todos


@app.get("/todos/{todo_id}")
def get_todo(
    todo_id: int,
    db: Session = Depends(get_db)
):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()

    if not todo:
        raise HTTPException(
            status_code=404,
            detail="Todo not found"
        )

    return todo