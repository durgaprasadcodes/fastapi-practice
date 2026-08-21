from fastapi import FastAPI, Request,HTTPException,status,Depends
from auth.auth import router
from database import get_db
from model import Users
from sqlalchemy.orm import Session
from JwtToken.dependencies import get_current_user
from limiter.limiter import limiter,RateLimitExceeded,_rate_limit_exceeded_handler
from schemas import Passwords

app = FastAPI()

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)
app.include_router(router=router)

@app.get("/hello")
@limiter.limit("5/minute")
async def hello(request: Request):
    return {"message": "Hello"}

@app.get("/current_user")
@limiter.limit("5/minute")
async def user_information(request: Request,payload:dict[str]=Depends(get_current_user),db:Session=Depends(get_db)):
    user_id = payload.get('sub',None)
    db_user = db.query(Users).filter(Users.id == user_id).first()
    if not db_user :
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_CONTENT,detail="User Not Found")
    return {
        'user':db_user.name,
        'email':db_user.email
    }