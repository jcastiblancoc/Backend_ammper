import requests
from requests.auth import HTTPBasicAuth
from config import API_KEY_ID, API_KEY_SECRET, BASE_URL_GET_INSTITUTIONS, BASE_URL_ACCOUNT_ID 
from fastapi import HTTPException


HEADERS = {
        "accept": "application/json"
    }

def get_bank_list():
    try:
        next_url = f"{BASE_URL_GET_INSTITUTIONS}?page_size=100"
        all_banks = []

        while next_url:
            response = requests.get(
                next_url,
                headers=HEADERS,
                auth=HTTPBasicAuth(API_KEY_ID, API_KEY_SECRET)
            )

            if response.status_code == 200:
                data = response.json()

                all_banks.extend(data.get("results", []))

                next_url = data.get("next")
            else:
                return {"error": response.status_code, "message": response.text}

        return {"banks": all_banks}

    except Exception as e:
        return {"error": "exception", "message": str(e)}

def get_balance(link_id):
    
    
    ingresos = 0
    egresos = 0

    next_url = f"{BASE_URL_ACCOUNT_ID}?link={link_id}&page_size=100"
    while next_url:
        response = requests.get(
            next_url,
            auth=HTTPBasicAuth(API_KEY_ID, API_KEY_SECRET),
            headers=HEADERS,
        )
        if response.status_code != 200:
            raise HTTPException(status_code=response.status_code, detail=response.text)

        data = response.json()
        
        if not data.get("results"):
            if data.get("next") is None:
                return {
                    "balance": 0,
                    "ingresos": 0,
                    "egresos": 0,
                }

        if not data.get("results"):
            raise HTTPException(status_code=404, detail="No se encontraron transacciones para el link_id proporcionado.")

        ingresos += sum(t["amount"] for t in data["results"] if t["type"] == "INFLOW")
        egresos += sum(t["amount"] for t in data["results"] if t["type"] == "OUTFLOW")

        next_url = data.get("next")
        
    balance = ingresos - egresos

    return {
        "balance": balance,
        "ingresos": ingresos,
        "egresos": egresos,
    }
