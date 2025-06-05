from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.dependencies import get_db
from backend.src.modules.applications.repository import ApplicationRepository
from backend.src.modules.applications.service import ApplicationService


def get_app_repo(session: AsyncSession = Depends(get_db)) -> ApplicationRepository:
    return ApplicationRepository(session=session)


def get_app_serv(application_repo: ApplicationRepository = Depends(get_app_repo)):
    return ApplicationService(application_repo=application_repo)
