from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

api = FastAPI()

class Todo(BaseModel):
    id: int
    name: str
    des: str

todos: List[Todo] = []

@api.get("/")
def index():
    return {"Message" : "Hello World"}


@api.get("/todo")
def get_todos():
    return todos


@api.post("/todo")
def add_todo(todo: Todo):
    todos.append(todo)
    return todos

@api.put("/todo/{todo_id}")
def update_todo(todo_id: int, updated_todo: Todo):
    for index, todo in enumerate(todos):
        if todo.id == todo_id:
            todos[index] = updated_todo
            return todos
    return {"error": "Todo Not Found"}


@api.delete("/todo/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todos):
        if todo.id==todo_id:
            deleted = todos.pop(index)
            return deleted
    
    return {"error":"Deleteion error"}