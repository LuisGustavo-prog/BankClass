from datetime import datetime, timedelta, timezone
from fastapi import HTTPException
from jose import JWTError, jwt
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN_SECRET_KEY = os.getenv('TOKEN_SECRET_KEY')
ALGORITHM = os.getenv('ALGORITHM ')
EXPIRE_HOURS = os.getenv('EXPIRE_HOURS')

def create_access_token(data: dict):
    payload = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(hours=EXPIRE_HOURS)
    payload.update({'exp': expire})

    token = jwt.encode(payload, TOKEN_SECRET_KEY, algorithm=ALGORITHM)
    return token

def decode_token(token: str):
    try:
        payload = jwt.decode(token, TOKEN_SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        raise HTTPException(status_code=401, detail='Token or expired.')
