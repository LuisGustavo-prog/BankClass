from src.core.employee_account import EmployeeClass
from src.database.connection import employee_accounts
from src.security.password_security import authenticate_password, change_password

async def login_employee(email: str, password: str):
    user = await employee_accounts.find_one({'email': email})

    if not user:
        raise ValueError('Not found.')

    authenticate_password(password=password, hashed_password=user['password'])

    return user['_id']

async def create_employee(name: str, email: str, password: str):
    user = EmployeeClass(name=name, email=email, password=password)

    try:
        await employee_accounts.insert_one(user.to_dict())
    except Exception as e:
        raise ValueError(f'Error saving user to database. {e}')

async def get_user(user_id: str):  
    try:
        user = await employee_accounts.find_one({'_id': user_id})
        
        if user is None:
            raise ValueError('User not found.')
        
        return user
    except Exception as e:
        raise ValueError(f'Error fetching user. {e}')

async def update_user(user_id: str, password: str, new_password: str): 
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])  
    fields_to_update = {}

    if new_password:
        fields_to_update['password'] = change_password(old_password=password, new_password=new_password, hashed_password=user['password'])

    if not fields_to_update:
        raise ValueError('No fields to update.')
    
    try:
        await employee_accounts.update_one(
            {'_id': user_id},
            {'$set': fields_to_update}
        )
    except Exception as e:
        raise ValueError(f'Error updating user. {e}')
    
async def delete_user(user_id: str, password: str):
    user = await get_user(user_id=user_id)
    authenticate_password(password=password, hashed_password=user['password'])

    try:
        await employee_accounts.delete_one({'_id': user_id})
    except Exception as e:
        raise ValueError(f'Error deleting user. {e}')
    