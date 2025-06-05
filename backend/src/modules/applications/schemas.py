import enum
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ConfigDict


class ServiceEnum(str, enum.Enum):
    repair: str = "repair"
    servers: str = "servers"
    one_c: str = "1C"
    other: str = "other"

    def __str__(self):
        return self.value


class StatusEnum(str, enum.Enum):
    cancel: str = "cancel"
    active: str = "active"
    in_progress: str = "in_progress"
    completed: str = "completed"

    def __str__(self):
        return self.value


class AppAddForm(BaseModel):
    service: ServiceEnum
    description: str


class ApplicationSchema(BaseModel):
    id: int
    user_id: int
    service: str
    description: str
    comment: Optional[str] = None
    status: StatusEnum
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

