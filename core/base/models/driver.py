from core.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from core.base.models import Road


class Driver(Base):
    __tablename__ = "driver"

    id_driver: Mapped[int] = mapped_column(primary_key=True)
    docs: Mapped[bool]
    name: Mapped[str] = mapped_column(String(50))

    road: Mapped["Road"] = relationship(back_populates="driver")
