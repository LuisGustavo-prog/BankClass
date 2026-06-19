from fastapi import APIRouter, Header
from src.controller.employee_controller import (
    get_user_bank_account_number_controller,
    get_all_user_bank_accounts_controller
)
from src.schema.employee_schema import GetUser, GetUsers

router = APIRouter(prefix="/employee", tags=["Employee"])

@router.get("/user")
async def get_user(data: GetUser, authorization: str = Header(...)):
    return await get_user_bank_account_number_controller(data=data, token=authorization)

@router.get("/users")
async def get_users(data: GetUsers, authorization: str = Header(...)):
    return await get_all_user_bank_accounts_controller(data=data, token=authorization)