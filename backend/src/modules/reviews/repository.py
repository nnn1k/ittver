from typing import Sequence

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import joinedload

from backend.src.database.models.reviews import ReviewModel


class ReviewRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create(self, company_name: str, service: str, rating: int, message: str, user_id: int):
        stmt = (
            insert(ReviewModel)
            .values(company_name=company_name, service=service, rating=rating, message=message, user_id=user_id)
            .returning(ReviewModel)
        )

        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def get_all(self, **kwargs) -> Sequence[ReviewModel]:
        stmt = (
            select(ReviewModel)
            .filter_by(**kwargs)
            .options(joinedload(ReviewModel.user))
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()

    async def get_one(self, **kwargs) -> ReviewModel:
        stmt = (
            select(ReviewModel)
            .filter_by(**kwargs)
            .options(joinedload(ReviewModel.user))
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()