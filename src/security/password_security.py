from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')

def creating_hash(password: str):
    return str(pwd_context.hash(password))

def authenticate_password(password: str, hashed_password: str):
    if not pwd_context.verify(password, hashed_password):
        raise HTTPException(status_code=401, detail='Error logging in.')

def change_password(old_password: str, new_password: str, hashed_password: str):
    if not pwd_context.verify(old_password, hashed_password):
        raise ValueError('Incorrect current password.')
    
    return creating_hash(new_password)
