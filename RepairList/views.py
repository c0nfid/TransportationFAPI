from typing import Literal

from fastapi import APIRouter, Depends, HTTPException
from pydantic import conint
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from RepairList import SRepairList, SRepairListBase, get_row_by_id
from core.base import db_helper
from core.base.models import RepairList

router = APIRouter(prefix="/repairs", tags=["Починочные листы"])


@router.get("/", response_model=list[SRepairList])
async def get_repair_list(
    order_field: Literal["id_list", "id_auto", "time"] = "id_list",
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    sort_field = getattr(RepairList, order_field)
    stmt = Select(RepairList).order_by(sort_field)
    response = await session.execute(stmt)
    return response.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SRepairList)
async def add_repair_row(
    repair_row: SRepairListBase,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = RepairList(**repair_row.model_dump())
    session.add(db_model)
    await session.commit()
    await session.refresh(db_model)
    return db_model


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def del_repair_row(
    id_list: conint(ge=1),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = await get_row_by_id(session, id_list)
    if db_model:
        await session.delete(db_model)
        await session.commit()

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Repair row with id:{id_list} not found",
        )
