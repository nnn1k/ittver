
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.base import Base, int_pk, created_at, updated_at
from backend.src.modules.applications.schemas import StatusEnum


class ApplicationModel(Base):
    __tablename__ = 'applications'

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    service: Mapped[str]
    description: Mapped[str]
    comment: Mapped[str] = mapped_column(nullable=True)
    status: Mapped[StatusEnum]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]
