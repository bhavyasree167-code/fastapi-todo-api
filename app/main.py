from fastapi import FastAPI
from .database import engine
from . import models
from .schemas import TodoCreate

app = FastAPI()

# Create database tables
models.Base.metadata.create_all(bind=engine)

todos = []

@app.get("/")
def root():
    return {"message": "API Running - Feature Branch"}


@app.post("/todos")
def create_todo(todo: TodoCreate):

    new_todo = {
        "id": len(todos) + 1,
        "title": todo.title,
        "completed": False
    }

    todos.append(new_todo)

    return new_todo


@app.get("/todos")
def get_todos():
    return todos

@app.put("/todos/{todo_id}")
def update_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todo["completed"] = True
            return todo

    return {"message": "Todo not found"}

@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for todo in todos:
        if todo["id"] == todo_id:
            todos.remove(todo)
            return {"message": "Todo deleted"}

    return {"message": "Todo not found"}