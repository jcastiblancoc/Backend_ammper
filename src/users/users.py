from fastapi import APIRouter, HTTPException, Request, Depends, Form
from connection import session
from models import User
from security import hash_password, get_user, create_access_token, verify_password, get_current_user

router = APIRouter()

@router.get("/")
async def get_users():
    return {"message": "List of users"}


@router.post("/register")
async def create_user(request: Request):
    user_data = await request.json()

    if not all(key in user_data for key in ["first_name", "last_name", "email", "phone", "password"]):
        raise HTTPException(status_code=400, detail="Faltan campos requeridos")

    if session.query(User).filter(User.email == user_data["email"]).first():
        raise HTTPException(status_code=400, detail="El usuario ya existe")

    new_user = User(
        first_name=user_data["first_name"],
        last_name=user_data["last_name"],
        email=user_data["email"],
        phone=user_data["phone"],
        password=hash_password(user_data["password"])
    )
    session.add(new_user)
    session.commit()
    session.refresh(new_user)

    return {"id": new_user.id, "message": "Usuario creado exitosamente"}


@router.post("/login/")
async def login(email: str = Form(...), password: str = Form(...)):
    user = session.query(User).filter(User.email == email).first()

    if user is None or not verify_password(password, user.password):
        raise HTTPException(status_code=401, detail="Credenciales incorrectas")

    access_token = create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/protected/")
async def protected_route(current_user: str = Depends(get_current_user)):
    return {"message": f"Bienvenido {current_user}"}
