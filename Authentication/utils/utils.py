from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"],deprecated = 'auto')

def hash_pwd(password:str)->str:
    return pwd_context.hash(password)
def verify_pwd(plane_pwd:str,hash_pwd:str)->bool:
    return pwd_context.verify(plane_pwd,hash_pwd)
