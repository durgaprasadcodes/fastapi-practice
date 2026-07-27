from fastapi import FastAPI,HTTPException,status,Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from contextlib import asynccontextmanager
import create_table


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table
    yield
    
app = FastAPI(lifespan=lifespan)

@app.get("/")
def home():
    return {"message":"Hi from FastAPI"}