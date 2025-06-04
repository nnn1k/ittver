from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory='frontend/pages/')

router = APIRouter(
    prefix="",
)


@router.get("/")
def main_page(request: Request):
    return templates.TemplateResponse("main/main.html", {"request": request})


@router.get("/lk")
def lk_page(request: Request):
    return templates.TemplateResponse("lk/lk.html", {"request": request})


@router.get("/auth")
def auth_page(request: Request):
    return templates.TemplateResponse("auth/auth.html", {"request": request})


@router.get("/register")
def register_page(request: Request):
    return templates.TemplateResponse("reg/reg.html", {"request": request})


@router.get("/swap_psw")
def swap_psw_page(request: Request):
    return templates.TemplateResponse("swap/swap_psw.html", {"request": request})


@router.post("/services")
def services_page(request: Request):
    return templates.TemplateResponse("services/services.html", {"request": request})


@router.get("/application")
def application_page(request: Request):
    return templates.TemplateResponse("application/application.html", {"request": request})


@router.get("/application_phone")
def application_phone_page(request: Request):
    return templates.TemplateResponse("application_phone/application_phone.html", {"request": request})