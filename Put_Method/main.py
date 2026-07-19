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
def my_tasks():
    return tasks

class Task(BaseModel):
    id:int
    task:str
    completed:bool
    
@app.put('/update/{id}')
def update_task(id:int,updated_task:Task):
    for task in tasks:
        if task['id'] == id:
            task["id"] = updated_task.id
            task["task"] = updated_task.task
            task["completed"] = updated_task.completed
            return task
    return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")