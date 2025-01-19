from fastapi import FastAPI
from src.users.users import router as users_router
from src.transactions.transactions import router as transactions_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="PWA Ammper Test")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(users_router, prefix="/api/v1/users", tags=["Users"])
app.include_router(transactions_router, prefix="/api/v1/transactions", tags=["Transactions"])
