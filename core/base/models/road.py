from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from core.base import Base

if TYPE_CHECKING:
    from core.base.models import Driver


class Road(Base):
    __tablename__ = "road"

    id_road: Mapped[int] = mapped_column(primary_key=True)
    id_auto: Mapped[int] = mapped_column(ForeignKey("auto.id_auto"))
    road_length: Mapped[int]
    start_point: Mapped[str] = mapped_column(String(18))
    end_point: Mapped[str] = mapped_column(String(18))
    id_driver: Mapped[int] = mapped_column(ForeignKey("driver.id_driver"))

    driver: Mapped["Driver"] = relationship(back_populates="road")
