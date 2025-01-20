from fastapi import FastAPI, APIRouter, HTTPException
from belvo import get_bank_list, get_balance


app = FastAPI()
router = APIRouter()

@router.get("/banks")
async def get_banks():
    data = get_bank_list()
    return data


@router.get("/banks/{link_id}/balance")
async def get_balance_and_transactions(link_id: str):
    try:
        return get_balance(link_id)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


app.include_router(router)