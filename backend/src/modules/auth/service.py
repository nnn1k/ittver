from fastapi import Response
from backend.src.modules.auth.exc import incorrect_login_or_password_exc, password_mismatch_exc, user_is_exist_exc
from backend.src.modules.auth.repository import AuthRepository
from backend.src.modules.auth.schemas import LoginForm, RegisterForm
from backend.src.modules.auth.utils import HashPwd, jwt_token
from backend.src.modules.users.schemas import UserSchema


class AuthService:

    def __init__(self, auth_repo: AuthRepository):
        self.auth_repo = auth_repo

    async def login(self, login_form: LoginForm, response: Response) -> UserSchema:
        user = await self.auth_repo.login(email=login_form.email)
        if not user:
            raise incorrect_login_or_password_exc
        if not HashPwd.validate_password(password=login_form.password, hashed_password=user.password):
            raise incorrect_login_or_password_exc
        schema = UserSchema.model_validate(user)
        self.create_token(response=response, user=schema)
        return schema

    async def register(self, register_form: RegisterForm, response: Response) -> UserSchema:
        if register_form.password != register_form.confirm_password:
            raise password_mismatch_exc
        old_user = await self.auth_repo.login(email=register_form.email)
        if old_user:
            raise user_is_exist_exc
        new_user = await self.auth_repo.register(
            name=register_form.name,
            surname=register_form.surname,
            email=register_form.email,
            hash_pwd=HashPwd.hash_password(register_form.password),
            phone=register_form.phone
        )
        schema = UserSchema.model_validate(new_user)
        self.create_token(response=response, user=schema)
        return schema

    async def logout(self, response: Response) -> None:
        response.delete_cookie('access_token')
        response.delete_cookie('refresh_token')

    @staticmethod
    def create_token(response: Response, user: UserSchema) -> None:
        access_token = jwt_token.create_access_token(payload={'id': user.id})
        refresh_token = jwt_token.create_refresh_token(payload={'id': user.id})

        response.set_cookie('access_token', access_token, max_age=60 * 60 * 24 * 365)
        response.set_cookie('refresh_token', refresh_token, max_age=60 * 60 * 24 * 365)
