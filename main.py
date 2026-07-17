from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

@app.get('/')
async def  read_root():
    return {"message":"Hello World"}

@app.get("/greet")
async def greet_name(name:Optional[str] = 'User' , age:int = 1)->dict:
    return {"message":f"Hello {name} Your Age is {age}"}

class Post(BaseModel):
    gender:str
    isPass:bool
    
@app.post('/post')
async def post_this(post:Post):
    return {
        "Gender":post.gender,
        "isPass":post.isPass
    }
