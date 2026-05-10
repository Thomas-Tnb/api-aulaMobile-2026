from fastapi import APIRouter, HTTPException
from uuid import uuid4

from app.schemas.auth import LoginRequest

router = APIRouter()


@router.post("/login")
def login(data: LoginRequest):

    if (
        data.email == "usuario@esoft.com"
        and data.password == "Abc123"
    ):
        return {
            "token": str(uuid4())
        }

    raise HTTPException(
        status_code=401,
        detail="Credenciais inválidas"
    )