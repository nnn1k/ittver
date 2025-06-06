from typing import Sequence

from backend.src.modules.reviews.exc import review_is_exist_exc
from backend.src.modules.reviews.repository import ReviewRepository
from backend.src.modules.reviews.schemas import AddReviewSchema, ReviewSchema
from backend.src.modules.users.schemas import UserSchema


class ReviewService:

    def __init__(self, review_repo: ReviewRepository):
        self.review_repo = review_repo

    async def create(self, form: AddReviewSchema, user: UserSchema) -> ReviewSchema:
        old_review = await self.review_repo.get_one(user_id=user.id, service=form.service)
        if old_review:
            raise review_is_exist_exc
        review = await self.review_repo.create(
            company_name=form.company_name,
            service=form.service,
            rating=form.rating,
            message=form.message,
            user_id=user.id
        )
        schema = ReviewSchema.model_validate(review)
        return schema

    async def get_all(self) -> Sequence[ReviewSchema]:
        reviews = await self.review_repo.get_all()
        return [ReviewSchema.model_validate(rev) for rev in reviews]



