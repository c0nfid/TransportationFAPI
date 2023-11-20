from fastapi import APIRouter, Depends, HTTPException
from pydantic import conint
from sqlalchemy import Select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status

from Model.crud import get_model_by_id
from Model.schemas import SModel, SModelBase
from core.base import db_helper
from core.base.models import Model

router = APIRouter(prefix="/models", tags=["Машиновые модели"])


@router.get("/", response_model=list[SModel])
async def get_model_list(
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    stmt = Select(Model).order_by(Model.id_model)
    response = await session.execute(stmt)
    return response.scalars().all()


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=SModel)
async def add_model(
    model: SModelBase,
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = Model(**model.model_dump())
    session.add(db_model)
    await session.commit()
    await session.refresh(db_model)
    return db_model


@router.delete("/", status_code=status.HTTP_204_NO_CONTENT, response_model=None)
async def del_model(
    id_model: conint(ge=1),
    session: AsyncSession = Depends(db_helper.session_dependency),
):
    db_model = await get_model_by_id(session, id_model)
    if db_model:
        await session.delete(db_model)
        await session.commit()

    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Model with id {id_model} not found",
        )
