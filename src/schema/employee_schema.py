from pydantic import BaseModel

class GetUser(BaseModel):
    user_id: str
    account_type: str

class GetUsers(BaseModel):
    account_type: str
