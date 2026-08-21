from utils.util import ALGORITHM, SECRET_KEY, EXPIRE_TIME
from datetime import datetime, timedelta, timezone
from jose import jwt


def create_access_token(source: dict) -> str:
    payload = source.copy()
    payload.update({'exp': datetime.now(timezone.utc) + timedelta(minutes=int(EXPIRE_TIME))})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def decode_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        if not payload.get('id'):
            raise ValueError("Incorrect Jwt Token")
    except Exception:
        raise ValueError("Incorrect Jwt Token")
    return payload
