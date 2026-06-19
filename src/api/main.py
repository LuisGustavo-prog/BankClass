from fastapi import FastAPI
from src.api.routes.checking_account_router import router as checking_router
from src.api.routes.saving_account_router import router as saving_router
from src.api.routes.auth_router import router as auth_router
from src.api.routes.employee_router import router as employee_router

app = FastAPI()

app.include_router(auth_router)
app.include_router(checking_router)
app.include_router(saving_router)
app.include_router(employee_router)
