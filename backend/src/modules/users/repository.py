from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import selectinload

from backend.src.database.models.users import UserModel


class UserRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_user(self, **kwargs) -> UserModel:
        stmt = (
            select(UserModel)
            .filter_by(**kwargs)
            .options(selectinload(UserModel.applications))
            .options(selectinload(UserModel.reviews))
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()
