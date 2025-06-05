from typing import List, Sequence

from sqlalchemy import insert, select
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.models.application import ApplicationModel
from backend.src.modules.applications.schemas import StatusEnum


class ApplicationRepository:

    def __init__(self, session: AsyncSession):
        self.session = session

    async def add(self, service: str, description: str, user_id: int) -> ApplicationModel:
        stmt = (
            insert(ApplicationModel)
            .values(user_id=user_id, service=service, description=description, status=StatusEnum.in_progress)
            .returning(ApplicationModel)
        )
        result = await self.session.execute(stmt)
        return result.scalars().first()

    async def get_all(self, **kwargs) -> Sequence[ApplicationModel]:
        stmt = (
            select(ApplicationModel)
            .filter_by(**kwargs)
        )
        result = await self.session.execute(stmt)
        return result.scalars().all()
