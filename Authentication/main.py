from fastapi import FastAPI
from contextlib import asynccontextmanager
import create_table
from routers.auth import router

@asynccontextmanager
async def lifespan(app:FastAPI):
    create_table
    yield
    
app = FastAPI(lifespan=lifespan)
app.include_router(router=router,tags=["auth"],prefix='/auth')
