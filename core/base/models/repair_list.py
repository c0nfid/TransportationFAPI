from typing import TYPE_CHECKING

from sqlalchemy.orm import Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey

from core.base import Base


if TYPE_CHECKING:
    from core.base.models import Auto


class RepairList(Base):
    __tablename__ = "repair_list"

    id_list: Mapped[int] = mapped_column(primary_key=True)
    id_auto: Mapped[int] = mapped_column(ForeignKey("auto.id_auto"))
    time: Mapped[str] = mapped_column(String(8))
    word: Mapped[str] = mapped_column(String(20))

    auto: Mapped["Auto"] = relationship(back_populates="repair_list")
