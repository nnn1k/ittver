from datetime import datetime
from typing import List, Optional

from pydantic import BaseModel, ConfigDict


class UserSchema(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    phone: str
    image_url: str
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)


class UserRelSchema(UserSchema):
    applications: Optional[List['ApplicationSchema']] = []
    reviews: Optional[List['ReviewSchema']] = []


class MessageForm(BaseModel):
    name: str
    phone: str
    message: str
    email_to: str = 'repost0099@gmail.com'