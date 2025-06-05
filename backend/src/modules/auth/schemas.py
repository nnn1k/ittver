from pydantic import BaseModel, EmailStr


class LoginForm(BaseModel):
    email: EmailStr
    password: str


class RegisterForm(BaseModel):
    email: EmailStr
    name: str
    surname: str
    phone: str
    password: str
    confirm_password: str
