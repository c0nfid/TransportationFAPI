from typing import Literal

from fastapi import APIRouter, Depends, HTTPException, Query
from pydantic import conint
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from Road import SRoad, SRoadBase, get_road_by_id
from core.base import db_helper
from core.base.models import Road

router = APIRouter(prefix="/roads", tags=["Тропиночные листы"])


@router.get("/", response_model=list[SRoad])
async def get_road_list(
    order_field: Literal["id_road", "id_auto", "road_length"] = "id_road",
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    sort_field = getattr(Road, order_field)
    stmt = Select(Road).order_by(sort_field)
    response = await session.execute(stmt)
    return response.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SRoad)
async def add_road(
    road: SRoadBase,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = Road(**road.model_dump())
    session.add(db_model)
    await session.commit()
    await session.refresh(db_model)
    return db_model


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def del_road(
    id_road: conint(ge=1),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = await get_road_by_id(session, id_road)
    if db_model:
        await session.delete(db_model)
        await session.commit()

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Repair row with id:{id_road} not found",
        )
