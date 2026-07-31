from fastapi import APIRouter
from schemas.user import UserInSignUp,UserInLogin,UserInUpdate,UserOutPut,UserWithToken
from services.service import signup_service,login_service
from sqlalchemy.orm import Session
from fastapi import Depends
from database import get_db

router = APIRouter()

@router.post('/login')
def login(loginDetails:UserInLogin,db: Session = Depends(get_db)):
    return login_service(loginDetails,db)

@router.post('/signup')
def signUp(signUpDetails:UserInSignUp,db: Session = Depends(get_db)):
    return signup_service(signUpDetails,db)