from fastapi import Depends, Cookie, Response, Query, Depends
from jwt import ExpiredSignatureError
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.dependencies import get_db
from backend.src.modules.auth.exc import invalid_token_exc, user_is_not_admin_exc
from backend.src.modules.auth.repository import AuthRepository
from backend.src.modules.auth.service import AuthService
from backend.src.modules.auth.utils import jwt_token
from backend.src.modules.users.dependencies import get_user_serv
from backend.src.modules.users.schemas import UserSchema
from backend.src.modules.users.service import UserService


def get_auth_repo(session: AsyncSession = Depends(get_db)) -> AuthRepository:
    return AuthRepository(session=session)


def get_auth_serv(auth_repo: AuthRepository = Depends(get_auth_repo)) -> AuthService:
    return AuthService(auth_repo=auth_repo)


async def get_user_by_token(
        access_token=Cookie(None, include_in_schema=False),
        refresh_token=Cookie(None, include_in_schema=False),
        response: Response = None,
        auth: bool = Query(True, include_in_schema=False),
        service: UserService = Depends(get_user_serv),
) -> UserSchema | None:
    user_id: int | None = None
    if access_token:
        try:
            user_id = jwt_token.decode_jwt(token=access_token).get("sub")
        except ExpiredSignatureError:
            print('access token expired')

    if not user_id and refresh_token:
        try:
            new_access_token, new_refresh_token = jwt_token.token_refresh(refresh_token)
            if not (new_access_token and new_refresh_token):
                raise invalid_token_exc

            user_id = jwt_token.decode_jwt(token=new_access_token).get("id")
            if not user_id:
                raise invalid_token_exc

            response.set_cookie(key='access_token', value=new_access_token)
            response.set_cookie(key='refresh_token', value=new_refresh_token)

        except ExpiredSignatureError:
            raise invalid_token_exc

    if not user_id:
        if auth:
            raise invalid_token_exc
        return None

    user = await service.get_user(id=int(user_id))
    return user


async def get_no_auth_user_by_token(
        access_token=Cookie(None, include_in_schema=False),
        refresh_token=Cookie(None, include_in_schema=False),
        response: Response = None,
        service: UserService = Depends(get_user_serv),
):
    return await get_user_by_token(
        access_token=access_token,
        refresh_token=refresh_token,
        response=response,
        auth=False,
        service=service,
    )
