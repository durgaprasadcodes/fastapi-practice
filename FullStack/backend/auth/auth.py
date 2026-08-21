from fastapi import APIRouter,Depends,HTTPException,status,Request
from schemas import Register,Login
from database import get_db
from sqlalchemy.orm import Session
from limiter.limiter import limiter
from utils.util import hash_pwd,verify_pwd
from model import Users
from JwtToken.token import create_access_token

router = APIRouter(tags=["Login Router"], prefix="/auth")

@router.post("/register", status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def register(request: Request,user: Register,db: Session = Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == user.email).first()

    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User already exists"
        )
    new_user = Users(name=user.name, email=user.email, password=hash_pwd(user.password))

    db.add(new_user)

    try:
        db.commit()
        db.refresh(new_user)

    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,detail=str(e.args))

    return {
        "message": "Registration successful"
    }

@router.post("/login", status_code=status.HTTP_200_OK)
@limiter.limit("5/minute")
async def login(request:Request,user:Login,db:Session=Depends(get_db)):
    db_user = db.query(Users).filter(Users.email == user.email).first()
    if not db_user or not verify_pwd(user.password,db_user.password):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="User or Password is Wrong ")
    
    token = create_access_token({'sub':str(db_user.id)})
    
    return {
        "access_token":token,
        "token_type":"bearer"
    }