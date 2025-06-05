from fastapi import APIRouter, Depends, Response

from backend.src.modules.auth.dependencies import get_auth_serv
from backend.src.modules.auth.schemas import LoginForm, RegisterForm
from backend.src.modules.auth.service import AuthService

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
)


@router.post("/login")
async def login(
        form: LoginForm,
        response: Response,
        service: AuthService = Depends(get_auth_serv)
):
    user = await service.login(login_form=form, response=response)
    return {"user": user}


@router.post("/register")
async def register(
        form: RegisterForm,
        response: Response,
        service: AuthService = Depends(get_auth_serv)
):
    user = await service.register(register_form=form, response=response)
    return {"user": user}


@router.post("/logout")
async def logout(
        response: Response,
        service: AuthService = Depends(get_auth_serv)
):
    await service.logout(response=response)
    return {"user": 'logged out'}