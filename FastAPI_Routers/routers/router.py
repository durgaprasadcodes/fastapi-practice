from fastapi import APIRouter
from schemes.scheme import UserInLogin,UserInSignUp

router = APIRouter()

@router.post("/login")
async def login(userDetails:UserInLogin):
    return {'Message':userDetails}

@router.post("/signup")
async def signUp(userDetails:UserInSignUp):
    return {"Message":userDetails}