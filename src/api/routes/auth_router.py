from fastapi import APIRouter
from src.controller.auth_controller import (
    register_checking_account_controller,
    register_saving_account_controller,
    checking_account_login_controller,
    saving_account_login_controller,
    register_employee_account_controller,
    checking_account_login_employee_controller  
)
from src.schema.auth_schema import CreateCheckingAccount, Login, LoginEmployee, CreateEmployee

router = APIRouter(prefix="/auth", tags=["Auth"])

@router.post("/register/checking")
async def register_checking(data: CreateCheckingAccount):
    await register_checking_account_controller(data=data)
    return {"message": "Checking account created successfully."}

@router.post("/register/saving")
async def register_saving(data: CreateCheckingAccount):
    await register_saving_account_controller(data=data)
    return {"message": "Saving account created successfully."}

@router.post("/login/checking")
async def login_checking(data: Login):
    token = await checking_account_login_controller(data=data)
    return {"access_token": token}

@router.post("/login/saving")
async def login_saving(data: Login):
    token = await saving_account_login_controller(data=data)
    return {"access_token": token}

@router.post("/register/employee")
async def register_employee(data: CreateEmployee):
    await register_employee_account_controller(data=data)
    return {"message": "Employee account created successfully."}

@router.post("/login/employee")
async def login_employee(data: LoginEmployee):
    token = await checking_account_login_employee_controller(data=data)  # ← nome atualizado
    return {"access_token": token}
