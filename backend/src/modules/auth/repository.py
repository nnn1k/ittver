from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.models.users import UserModel


class AuthRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def login(self, email: str) -> UserModel:
        stmt = (
            select(UserModel)
            .filter_by(email=email)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def register(self, name: str, surname: str, email: str, hash_pwd: bytes, phone: str) -> UserModel:
        stmt = (
            insert(UserModel)
            .values(name=name, surname=surname, email=email, password=hash_pwd, phone=phone)
            .returning(UserModel)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

