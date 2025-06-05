from datetime import datetime

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
