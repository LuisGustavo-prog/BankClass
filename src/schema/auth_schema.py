from pydantic import BaseModel

class Login(BaseModel):
    account_number: str
    password: str

class CreateCheckingAccount(BaseModel):
    cardholder_name: str
    password: str
    
class LoginEmployee(BaseModel):
    email: str
    password: str

class CreateEmployee(BaseModel):
    name: str
    email: str
    password: str