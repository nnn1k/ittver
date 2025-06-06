from fastapi import APIRouter, Depends

from backend.src.modules.auth.dependencies import get_user_by_token, get_no_auth_user_by_token
from backend.src.modules.reviews.dependencies import get_review_serv
from backend.src.modules.reviews.schemas import AddReviewSchema
from backend.src.modules.reviews.services import ReviewService
from backend.src.modules.users.schemas import UserSchema

router = APIRouter(
    prefix="/reviews",
    tags=["reviews"],
)


@router.get("")
async def get_reviews(
        service: ReviewService = Depends(get_review_serv),
        user: UserSchema = Depends(get_no_auth_user_by_token),
):
    reviews = await service.get_all()
    return {
        "1C": [rev for rev in reviews if rev.service == "1C"],
        "repair": [rev for rev in reviews if rev.service == "repair"],
        "servers": [rev for rev in reviews if rev.service == "servers"],
        "other": [rev for rev in reviews if rev.service == "other"],
        "all": reviews,
        "user": user
    }


@router.post("")
async def create_review(
        form: AddReviewSchema,
        user: UserSchema = Depends(get_user_by_token),
        service: ReviewService = Depends(get_review_serv),
):
    review = await service.create(form=form, user=user)
    return {"review": review}
