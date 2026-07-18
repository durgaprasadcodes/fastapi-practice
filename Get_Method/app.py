from fastapi import FastAPI , HTTPException ,status
from typing import Optional
from pydantic import BaseModel


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

app = FastAPI()


@app.get("/")
def get_books():
    return tasks
  
@app.get('/profile/{name}')
def profile(name:str):
  return f"Username : {name}"

@app.get('/user')
def printName(name:Optional[str]="User",age:Optional[int]=None):
  return f"UserName : {name} \n Age : {age}"

@app.get("/getbook/{id}")
def get_book(id:int):
  for task in tasks:
    if task["id"] == id:
      return task

  return HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="Book Not Found")