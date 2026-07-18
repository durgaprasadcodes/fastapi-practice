from fastapi import FastAPI , HTTPException ,status
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


class Task(BaseModel):
    id:int
    task:str
    completed:bool
    
@app.get('/tasks')
def get_tasks():
    return tasks

@app.post('/posttask')
def post(task:Task):
    tasks.append(task)
    return {
        "id":task.id,
        "task":task.task,
        "completed":task.completed
    }
    
