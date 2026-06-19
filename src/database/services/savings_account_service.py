from datetime import datetime
from src.core.investment import Investment
from src.core.savings_account import SavingAccount
from src.database.connection import savings_accounts
from src.security.password_security import authenticate_password
from src.database.repository.savings_account_repository import get_user

def build_account(user: dict):
    account = SavingAccount(
        cardholder_name=user['cardholder_name'],
        password='password'
    )
    account._password = user['password']
    account._debit = user['debit']
    account._transaction_history = user['transaction_history']

    investments = []
    for i in user['investments']:
        obj = Investment(value=i['value'], duration_days=i['duration_days'], rate=i['rate'])
        obj._start_date = datetime.fromisoformat(i['start_date'])
        investments.append(obj)

    account._investments = investments
    return account

async def withdraw(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.withdraw(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await savings_accounts.update_one({'_id': user_id}, {'$set': data})

async def deposit(user_id: str, password: str, value: float | int):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.deposit(value=value)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await savings_accounts.update_one({'_id': user_id}, {'$set': data})

async def invest(user_id: str, value: float | int, duration_days: int, password: str):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.invest(value=value, duration_days=duration_days)

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await savings_accounts.update_one({'_id': user_id}, {'$set': data})

async def redeem_investment(user_id: str, password: str):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    account = build_account(user=user)
    account.redeem_investment()

    data = account.to_dict()
    data.pop('_id')
    data.pop('password')
    await savings_accounts.update_one({'_id': user_id}, {'$set': data})
