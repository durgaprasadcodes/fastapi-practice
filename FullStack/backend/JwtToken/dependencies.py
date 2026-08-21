from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends,HTTPException,status
from .token import decode_access_token 
from jose import JWTError

scheme_outh = OAuth2PasswordBearer(tokenUrl="auth/login")

async def get_current_user(token:str = Depends(scheme_outh)):
    try:
        payload = decode_access_token(token)
        if not payload:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired access token")
        return payload
    except JWTError:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Invalid or expired access token")