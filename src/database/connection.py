from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
import os

load_dotenv()

MONGO_URL = os.getenv('MONGO_URL')

client = AsyncIOMotorClient(MONGO_URL)
db = client['Bank']

checking_accounts = db['CheckingAccount']
savings_accounts = db['SavingAccount']
employee_accounts = db['EmployeeAccounts']

async def check_mongo():
    try:
        await client.admin.command('ping')
        
        return True
    except Exception as e:
        raise ValueError(f'Error connecting to the database. {e}')
    