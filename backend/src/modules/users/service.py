from backend.src.modules.users.repository import UserRepository
from backend.src.modules.users.schemas import UserSchema, UserRelSchema


class UserService:

    def __init__(self, user_repo: UserRepository):
        self.user_repo = user_repo

    async def get_user(self, **kwargs) -> UserSchema:
        user = await self.user_repo.get_user(**kwargs)
        schema = UserSchema.model_validate(user)
        return schema

    async def get_user_rel(self, **kwargs) -> UserRelSchema:
        user = await self.user_repo.get_user(**kwargs)
        schema = UserRelSchema.model_validate(user)
        return schema