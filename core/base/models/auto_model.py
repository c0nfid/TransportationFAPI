from core.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .auto import Auto


class Model(Base):
    __tablename__ = "auto_model"

    id_model: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(18))
    vendor_country: Mapped[str] = mapped_column(String(18))

    autos: Mapped["Auto"] = relationship(back_populates="model")

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name
