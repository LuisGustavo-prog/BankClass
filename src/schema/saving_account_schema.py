from pydantic import BaseModel

class SavingAccountUpdate(BaseModel):
    user_id: str
    password: str
    new_cardholder_name: str = None 
    new_password: str = None

class SavingAccountDelete(BaseModel):
    user_id: str
    password: str

class SavingAccountWithdraw(BaseModel):
    user_id: str
    password: str
    value: float | int

class SavingAccountDeposit(BaseModel):
    user_id: str
    password: str
    value: float | int

class SavingAccountInvest(BaseModel):
    user_id:str
    value: float | int
    duration_days: int
    password: str

class SavingAccountRedeemInvestment(BaseModel):
    user_id: str
    password: str