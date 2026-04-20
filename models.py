# ORM model definitions; Base is imported from database.py to share the same metadata.
from sqlalchemy.orm import Mapped, mapped_column
from database import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    email: Mapped[str] = mapped_column(unique=True, nullable=False)
    image_file: Mapped[str] = mapped_column(nullable=True)

    @property
    def image_url(self):
        if self.image_file:
            return f"/static/images/{self.image_file}"
        return "/static/images/default.jpg"
