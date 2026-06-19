from pydantic import BaseModel

class CheckingAccountUpdate(BaseModel):
    user_id: str
    password: str
    new_cardholder_name: str = None 
    new_password: str = None

class CheckingAccountDelete(BaseModel):
    user_id: str
    password: str

class CheckingAccountWithdraw(BaseModel):
    user_id: str
    password: str
    value: float | int

class CheckingAccountDeposit(BaseModel):
    user_id: str
    password: str
    value: float | int

class CheckingAccountDebitPayment(BaseModel):
    user_id: str
    password: str
    value: float | int

class CheckingAccountCreditPayment(BaseModel):
    user_id: str
    password: str
    value: float | int
    