from typing import Literal


from fastapi import APIRouter, Depends, HTTPException
from pydantic import conint
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import Select
from sqlalchemy.orm import joinedload
from starlette import status

from Auto.schemas import SAutoWithModel
from core.base import db_helper
from core.base.models import Auto, Model

from Auto import get_auto_by_id
from Auto import SAutoBase, SAuto, join_table

router = APIRouter(prefix="/autos", tags=["Машиновы"])


@router.get("/", response_model=list[SAuto])
async def get_auto_list(
    order_field: Literal["id_auto", "capacity"] = "id_auto",
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    sort_field = getattr(Auto, order_field)
    stmt = Select(Auto).order_by(Auto.id_auto)
    response = await session.execute(stmt)
    return response.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SAuto)
async def add_auto(
    auto: SAutoBase,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    raw = Auto(**auto.model_dump())
    session.add(raw)
    await session.commit()
    await session.refresh(raw)
    return raw


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def del_auto(
    id_auto: conint(ge=1),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    auto_model: Auto | None = await get_auto_by_id(session=session, auto_id=id_auto)
    if auto_model:
        await session.delete(auto_model)
        await session.commit()
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@router.get("/with_models", response_model=list[SAutoWithModel])
async def get_auto_with_models_list(
    order_field: Literal["id_auto", "capacity", "name", "vendor_country"] = "id_auto",
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    sort_field = (
        getattr(Auto, order_field)
        if order_field in Auto.__dir__(Auto())
        else getattr(Model, order_field)
    )
    # stmt = Select(Auto).options(joinedload(Auto.model))

    if order_field in Model.__dir__(Model()):
        stmt = Select(Auto).options(joinedload(Auto.model))
        jnt = True  # костыль
    else:
        stmt = Select(Auto).options(joinedload(Auto.model)).order_by(sort_field)
        jnt = False

    response = await session.execute(stmt)
    autos = response.scalars().all()
    autos = await join_table(autos, order_field, jnt)
    return autos
