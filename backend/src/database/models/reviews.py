
from sqlalchemy import ForeignKey

from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.src.database.base import Base, int_pk, created_at, updated_at
from backend.src.modules.applications.schemas import StatusEnum, ServiceEnum


class ReviewModel(Base):
    __tablename__ = 'reviews'

    id: Mapped[int_pk]
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    company_name: Mapped[str] = mapped_column(nullable=True)
    service: Mapped[ServiceEnum]
    rating: Mapped[int]
    message: Mapped[str]
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]

    user: Mapped['UserModel'] = relationship(
        'UserModel',
        back_populates='reviews',
        lazy='noload'
    )

