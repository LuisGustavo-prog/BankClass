from fastapi import HTTPException
from src.token.jwt import decode_token
from src.schema.employee_schema import GetUser, GetUsers
from src.database.repository.checking_account_repository import (
    get_user as get_user_checking_account,
    get_users as get_users_checking_account
)
from src.database.repository.savings_account_repository import (
    get_user as get_user_saving_account,
    get_users as get_users_saving_account
)

async def get_user_bank_account_number_controller(data: GetUser, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'employee':
        raise HTTPException(status_code=403, detail="Access denied.")

    account_type = data.account_type.lower()
    
    if account_type != 'checking account' and account_type != 'savings account':
        raise ValueError('Invalid account types.')
    
    if account_type == 'checking account':
        return await get_user_checking_account(user_id=data.user_id)
    
    if account_type == 'savings account':
        return await get_user_saving_account(user_id=data.user_id)
    
async def get_all_user_bank_accounts_controller(data: GetUsers, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'employee':
        raise HTTPException(status_code=403, detail="Access denied.")

    account_type = data.account_type.lower()
    
    if account_type != 'checking account' and account_type != 'savings account':
        raise ValueError('Invalid account types.')
    
    if account_type == 'checking account':
        return await get_users_checking_account()

    if account_type == 'savings account':
        return await get_users_saving_account()