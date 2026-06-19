from src.schema.checking_account_schema import CheckingAccountCreditPayment, CheckingAccountDebitPayment, CheckingAccountDelete, CheckingAccountDeposit, CheckingAccountUpdate, CheckingAccountWithdraw
from src.database.repository.checking_account_repository import update_user, delete_user
from src.database.services.checking_account_service import credit_payment, debit_payment, withdraw, deposit
from src.token.jwt import decode_token

async def update_controller(data: CheckingAccountUpdate, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await update_user(user_id=data.user_id, password=data.password, new_cardholder_name=data.new_cardholder_name, new_password=data.new_password)

async def delete_controller(data: CheckingAccountDelete, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await delete_user(user_id=data.user_id, password=data.password)

async def credit_payment_controller(data: CheckingAccountCreditPayment, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await credit_payment(user_id=data.user_id, password=data.password, value=data.value)

async def debit_payment_controller(data: CheckingAccountDebitPayment, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await debit_payment(user_id=data.user_id, password=data.password, value=data.value)

async def withdraw_controller(data: CheckingAccountWithdraw, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')
    
    await withdraw(user_id=data.user_id, password=data.password, value=data.value)

async def deposit_controller(data: CheckingAccountDeposit, token: str):
    payload = decode_token(token=token)

    if payload['role'] != 'client':
        raise ValueError('Invalid account types.')

    await deposit(user_id=data.user_id, password=data.password, value=data.value)
    