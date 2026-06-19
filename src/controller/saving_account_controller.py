from src.schema.saving_account_schema import SavingAccountDelete, SavingAccountDeposit, SavingAccountInvest, SavingAccountRedeemInvestment, SavingAccountUpdate, SavingAccountWithdraw
from src.database.services.savings_account_service import withdraw, deposit, invest, redeem_investment
from src.database.repository.savings_account_repository import update_user, delete_user
from src.token.jwt import decode_token

async def update_controller(data: SavingAccountUpdate, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')

    await update_user(user_id=data.user_id, password=data.password, new_cardholder_name=data.new_cardholder_name, new_password=data.new_password)

async def delete_controller(data: SavingAccountDelete, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
        
    await delete_user(user_id=data.user_id, password=data.password)

async def withdraw_controller(data: SavingAccountWithdraw, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await withdraw(user_id=data.user_id, password=data.password, value=data.value)

async def deposit_controller(data: SavingAccountDeposit, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await deposit(user_id=data.user_id, password=data.password, value=data.value)

async def invest_controller(data: SavingAccountInvest, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await invest(user_id=data.user_id, value=data.value, duration_days=data.duration_days, password=data.password)

async def redeem_investment_controller(data: SavingAccountRedeemInvestment, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await redeem_investment(user_id=data.user_id, password=data.password)
