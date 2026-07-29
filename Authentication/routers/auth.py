from fastapi import APIRouter
from schemas.user import UserInSignUp,UserInLogin,UserInUpdate,UserOutPut,UserWithToken

router = APIRouter()

@router.post('/login')
def login(loginDetails:UserInLogin):
    return {"data":loginDetails}

@router.post('/signup')
def signUp(signUpDetails:UserInSignUp):
    return {"data":signUpDetails}