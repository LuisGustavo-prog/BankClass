from fastapi import APIRouter, Header
from src.controller.saving_account_controller import (
    update_controller,
    delete_controller,
    withdraw_controller,
    deposit_controller,
    invest_controller,
    redeem_investment_controller
)
from src.schema.saving_account_schema import (
    SavingAccountUpdate,
    SavingAccountDelete,
    SavingAccountWithdraw,
    SavingAccountDeposit,
    SavingAccountInvest,
    SavingAccountRedeemInvestment
)

router = APIRouter(prefix="/saving", tags=["Saving Account"])

@router.put("/update")
async def update(data: SavingAccountUpdate, authorization: str = Header(...)):
    await update_controller(data=data, token=authorization)
    return {"message": "Account updated successfully."}

@router.delete("/delete")
async def delete(data: SavingAccountDelete, authorization: str = Header(...)):
    await delete_controller(data=data, token=authorization)
    return {"message": "Account deleted successfully."}

@router.put("/withdraw")
async def withdraw(data: SavingAccountWithdraw, authorization: str = Header(...)):
    await withdraw_controller(data=data, token=authorization)
    return {"message": "Withdraw completed successfully."}

@router.post("/deposit")
async def deposit(data: SavingAccountDeposit, authorization: str = Header(...)):
    await deposit_controller(data=data, token=authorization)
    return {"message": "Deposit completed successfully."}

@router.post("/invest")
async def invest(data: SavingAccountInvest, authorization: str = Header(...)):
    await invest_controller(data=data, token=authorization)
    return {"message": "Investment created successfully."}

@router.put("/redeem")
async def redeem_investment(data: SavingAccountRedeemInvestment, authorization: str = Header(...)):
    await redeem_investment_controller(data=data, token=authorization)
    return {"message": "Investment redeemed successfully."}
