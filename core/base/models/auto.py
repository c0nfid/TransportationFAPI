from core.base import Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from .auto_model import Model
    from .repair_list import RepairList


class Auto(Base):
    __tablename__ = "auto"

    id_auto: Mapped[int] = mapped_column(primary_key=True)
    id_model: Mapped[int] = mapped_column(ForeignKey("auto_model.id_model"))
    capacity: Mapped[int]
    docs: Mapped[bool]

    model: Mapped["Model"] = relationship(back_populates="autos")
    repair_list: Mapped["RepairList"] = relationship(back_populates="auto")
