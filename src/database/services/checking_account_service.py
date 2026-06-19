from src.core.checkingAccount import CheckingAccount
from src.database.connection import checking_accounts
from src.security.password_security import authenticate_password
from src.database.repository.checking_account_repository import get_user

def build_account(user: dict):
    account = CheckingAccount(
        cardholder_name=user['cardholder_name'],
        password='password'
    )
    account._password = user['password']
    account._debit = user['debit']
    account._credit = user['credit']
    account._transaction_history = user['transaction_history']
    return account

async def withdraw(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.withdraw(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await checking_accounts.update_one({'_id': user_id}, {'$set': data})

async def deposit(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.deposit(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await checking_accounts.update_one({'_id': user_id}, {'$set': data})

async def debit_payment(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.debit_payment(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await checking_accounts.update_one({'_id': user_id}, {'$set': data})

async def credit_payment(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.credit_payment(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await checking_accounts.update_one({'_id': user_id}, {'$set': data})
