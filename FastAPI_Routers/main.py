from fastapi import FastAPI
from routers.router import router
from slowapi import Limiter

app = FastAPI()
app.include_router(router=router,tags=['Auth'],prefix='/auth')

@app.get("/")
def hello():
    return {'message':'Hello From FastAPI'}