from typing import Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import conint
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from core.base import db_helper
from core.base.models import Driver
from Driver import get_driver_by_id
from Driver import SDriver, SDriverBase


router = APIRouter(prefix="/drivers", tags=["Шофёровы"])


@router.get("/", response_model=list[SDriver])
async def get_driver_list(
    order_field: Literal["id_driver", "name"] = "id_driver",
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    sort_field = getattr(Driver, order_field)
    stmt = Select(Driver).order_by(sort_field)
    response = await session.execute(stmt)
    return response.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SDriver)
async def add_driver(
    auto: SDriverBase,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    raw = Driver(**auto.model_dump())
    session.add(raw)
    await session.commit()
    await session.refresh(raw)
    return raw


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def del_driver(
    id_driver: conint(ge=1),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    driver_model: Driver | None = await get_driver_by_id(
        session=session, id_driver=id_driver
    )
    if driver_model:
        await session.delete(driver_model)
        await session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
