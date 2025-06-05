from fastapi import APIRouter, Depends

from backend.src.modules.auth.dependencies import get_user_by_token
from backend.src.modules.users.schemas import UserSchema

router = APIRouter(
    prefix="/users",
    tags=["users"],
)


@router.get('/me')
async def get_user(
        user: UserSchema = Depends(get_user_by_token)
):
    return {'user': user}
