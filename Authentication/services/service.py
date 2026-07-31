from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from model import User
from utils.utils import hash_pwd,verify_pwd
from schemas.user import UserInSignUp,UserInLogin
from auth_token.jwt_token import create_acces_token

def signup_service(user:UserInSignUp,db:Session):
    existing = db.query(User).filter(User.email == user.email).first()

    if existing:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,detail="Email already registered")

    hashed_password = hash_pwd(user.password)

    new_user = User(name=user.name,email=user.email,password=hashed_password)

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return {"message": "User created successfully"}

    
def login_service(user:UserInLogin,db:Session):
    db_user = db.query(User).filter(User.email == user.email).first()

    if not db_user or not verify_pwd(user.password,db_user.password):
        raise HTTPException(status_code=401,detail="Invalid email or password")

    token = create_acces_token({'sub':db_user.email})
    
    return {
    "access_token": token,
    "token_type": "bearer"
}
