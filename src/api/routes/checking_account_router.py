# src/routes/checking_account_router.py
from fastapi import APIRouter, Header
from src.controller.checking_account_controller import (
    update_controller,
    delete_controller,
    credit_payment_controller,
    debit_payment_controller,
    withdraw_controller,
    deposit_controller
)
from src.schema.checking_account_schema import (
    CheckingAccountUpdate,
    CheckingAccountDelete,
    CheckingAccountCreditPayment,
    CheckingAccountDebitPayment,
    CheckingAccountWithdraw,
    CheckingAccountDeposit
)

router = APIRouter(prefix="/checking", tags=["Checking Account"])

@router.put("/update")
async def update(data: CheckingAccountUpdate, authorization: str = Header(...)):
    await update_controller(data=data, token=authorization)
    return {"message": "Account updated successfully."}

@router.delete("/delete")
async def delete(data: CheckingAccountDelete, authorization: str = Header(...)):
    await delete_controller(data=data, token=authorization)
    return {"message": "Account deleted successfully."}

@router.post("/deposit")
async def deposit(data: CheckingAccountDeposit, authorization: str = Header(...)):
    await deposit_controller(data=data, token=authorization)
    return {"message": "Deposit completed successfully."}

@router.put("/withdraw")
async def withdraw(data: CheckingAccountWithdraw, authorization: str = Header(...)):
    await withdraw_controller(data=data, token=authorization)
    return {"message": "Withdraw completed successfully."}

@router.post("/credit-payment")
async def credit_payment(data: CheckingAccountCreditPayment, authorization: str = Header(...)):
    await credit_payment_controller(data=data, token=authorization)
    return {"message": "Credit payment completed successfully."}

@router.post("/debit-payment")
async def debit_payment(data: CheckingAccountDebitPayment, authorization: str = Header(...)):
    await debit_payment_controller(data=data, token=authorization)
    return {"message": "Debit payment completed successfully."}