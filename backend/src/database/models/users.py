from sqlalchemy.orm import Mapped, mapped_column

from backend.src.database.base import Base, int_pk, created_at, updated_at


class UserModel(Base):
    __tablename__ = 'users'

    id: Mapped[int_pk]
    name: Mapped[str] = mapped_column(nullable=True)
    surname: Mapped[str] = mapped_column(nullable=True)
    email: Mapped[str]
    password: Mapped[bytes]
    phone: Mapped[str]
    image_url: Mapped[str] = mapped_column(default='')
    created_at: Mapped[created_at]
    updated_at: Mapped[updated_at]


