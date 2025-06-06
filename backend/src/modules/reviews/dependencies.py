from fastapi import Depends
from sqlalchemy.ext.asyncio import AsyncSession

from backend.src.database.dependencies import get_db
from backend.src.modules.reviews.repository import ReviewRepository
from backend.src.modules.reviews.services import ReviewService


def get_review_repo(session: AsyncSession = Depends(get_db)) -> ReviewRepository:
    return ReviewRepository(session=session)


def get_review_serv(review_repo: ReviewRepository = Depends(get_review_repo)) -> ReviewService:
    return ReviewService(review_repo=review_repo)
