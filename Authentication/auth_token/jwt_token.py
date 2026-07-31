from jose import jwt
from datetime import datetime,timedelta

SECRECT_KEY = "53e9b65199f932f93806d748c2ac314e5202a9a399a4008b39e8b2c9f4bdb415"
ALGORTHIM = "HS256"
EXPIRE_TIME = 30

def create_acces_token(data:dict):
    to_encode = data.copy()
    to_encode.update({'exp':datetime.utcnow()+timedelta(minutes=EXPIRE_TIME)})
    return jwt.encode(to_encode,SECRECT_KEY,algorithm=ALGORTHIM)