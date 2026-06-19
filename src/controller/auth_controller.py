from src.token.jwt import create_access_token
from src.database.repository.employee_repository import create_employee, login_employee
from src.schema.auth_schema import CreateCheckingAccount, Login, LoginEmployee, CreateEmployee
from src.database.repository.savings_account_repository import create_user_savings_accounts, login_saving
from src.database.repository.checking_account_repository import create_user_checking_accounts, login_checking

async def register_checking_account_controller(data: CreateCheckingAccount):
    await create_user_checking_accounts(cardholder_name=data.cardholder_name, password=data.password)

async def register_saving_account_controller(data: CreateCheckingAccount):
    await create_user_savings_accounts(cardholder_name=data.cardholder_name, password=data.password)

async def checking_account_login_controller(data: Login):
    user_id = await login_checking(account_number=data.account_number, password=data.password)
    return create_access_token(data={'_id': user_id, 'role': 'client'})

async def saving_account_login_controller(data: Login):
    user_id = await login_saving(account_number=data.account_number, password=data.password)
    return create_access_token(data={'_id': user_id, 'role': 'client'})

# employee
async def register_employee_account_controller(data: CreateEmployee):
    await create_employee(name=data.name, email=data.email, password=data.password)  

async def checking_account_login_employee_controller(data: LoginEmployee):
    user_id = await login_employee(email=data.email, password=data.password)
    return create_access_token(data={'_id': user_id, 'role': 'employee'})

