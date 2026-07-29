from fastapi import FastAPI,HTTPException,status,Depends
from database import get_db
from sqlalchemy.orm import Session
import model
from contextlib import asynccontextmanager
import create_table
from routers.auth import login,signUp,router


@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table
    yield
    
app = FastAPI(lifespan=lifespan)
app.include_router(router=router,tags=["auth"],prefix='/auth')

@app.get("/")
def home():
    return {"message":"Hi from FastAPI"}