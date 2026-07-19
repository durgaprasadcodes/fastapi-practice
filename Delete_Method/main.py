from fastapi import FastAPI,HTTPException,status
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

tasks = [
  {
    "id": 1,
    "task": "Learn FastAPI Basics",
    "completed": False
  },
  {
    "id": 2,
    "task": "Build CRUD API",
    "completed": False
  },
  {
    "id": 3,
    "task": "Connect PostgreSQL Database",
    "completed": False
  },
  {
    "id": 4,
    "task": "Implement JWT Authentication",
    "completed": False
  },
  {
    "id": 5,
    "task": "Deploy FastAPI Project",
    "completed": False
  }
]

@app.get("/")
def get_tasks():
    return tasks

@app.delete("/deleteTask/{task_id}")
def delete(id:int):
    for task in tasks:
        if task["id"] == id:
            tasks.remove(task)
            return { "message":"Book Deleted Succesfully"}
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not found")
