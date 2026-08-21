from dotenv import load_dotenv
from pwdlib import PasswordHash
import os

load_dotenv()
pwd_manager = PasswordHash.recommended()

DATABASE_URL = os.getenv('DATABASE_URL')
SECRET_KEY = os.getenv('SECRET_KEY') or 'your_super_secret_key_here'
ALGORITHM = os.getenv('ALGORITHM')  
EXPIRE_TIME = os.getenv('EXPIRE_TIME')
ALGORTHIM = ALGORITHM

def hash_pwd(password:str)->str:
    return pwd_manager.hash(password)
def verify_pwd(password:str,db_password:str)->bool:
    return pwd_manager.verify(password,db_password)