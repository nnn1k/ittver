from datetime import datetime
from typing import Optional

from pydantic import BaseModel, field_validator, ConfigDict

from backend.src.modules.applications.schemas import ServiceEnum
from backend.src.modules.reviews.exc import review_bad_rating_exc


class ReviewSchema(BaseModel):
    id: int
    user_id: int
    company_name: Optional[str] = ''
    service: ServiceEnum
    rating: int
    message: str
    created_at: datetime
    updated_at: datetime

    user: Optional['UserSchema'] = None

    model_config = ConfigDict(from_attributes=True)


class AddReviewSchema(BaseModel):
    company_name: Optional[str] = ''
    service: ServiceEnum
    rating: int = 5
    message: str

    @field_validator('rating')
    def validate_rating(cls, v):
        if not 1 <= v <= 5:
            raise review_bad_rating_exc
        return v
