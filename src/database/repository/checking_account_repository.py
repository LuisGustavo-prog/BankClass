from fastapi import HTTPException
from src.core.checkingAccount import CheckingAccount
from src.database.connection import checking_accounts
from src.security.password_security import authenticate_password, change_password

async def login_checking(account_number: str, password: str):
    user = await checking_accounts.find_one({'account_number': account_number})

    if not user:
        raise HTTPException(status_code=401, detail='Invalid credentials')

    authenticate_password(password=password, hashed_password=user['password'])

    return user['_id']

async def create_user_checking_accounts(cardholder_name: str, password: str):
    object_current_account = CheckingAccount(cardholder_name=cardholder_name, password=password)

    try:
        await checking_accounts.insert_one(object_current_account.to_dict())
    except Exception as e:
        raise ValueError(f'Error saving user to database. {e}')

async def get_user(user_id: str):  
    try:
        user = await checking_accounts.find_one({'_id': user_id})
        
        if user is None:
            raise ValueError('User not found.')
        
        return user
    except Exception as e:
        raise ValueError(f'Error fetching user. {e}')

async def get_users(): 
    try:
        users = await checking_accounts.find().to_list(length=None)
        
        if not users:
            raise ValueError('No users found.')
        
        return users
    except Exception as e:
        raise ValueError(f'Error fetching users. {e}')

async def update_user(user_id: str, password: str, new_cardholder_name: str = None, new_password: str = None): 
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])  
    fields_to_update = {}

    if new_cardholder_name:
        fields_to_update['cardholder_name'] = new_cardholder_name

    if new_password:
        fields_to_update['password'] = change_password(old_password=password, new_password=new_password, hashed_password=user['password'])

    if not fields_to_update:
        raise ValueError('No fields to update.')

    try:
        await checking_accounts.update_one(
            {'_id': user_id},
            {'$set': fields_to_update}
        )
    except Exception as e:
        raise ValueError(f'Error updating user. {e}')

async def delete_user(user_id: str, password: str):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    try:
        await checking_accounts.delete_one({'_id': user_id})
    except Exception as e:
        raise ValueError(f'Error deleting user. {e}')
    