from core.base.models import Model
from sqlalchemy.ext.asyncio import AsyncSession
from .schemas import SUpdateModel


async def get_model_by_id(session: AsyncSession, model_id: int) -> Model | None:
    return await session.get(Model, model_id)


async def update_model(
    session: AsyncSession, db_model: Model, new_model: SUpdateModel
) -> Model:
    for field, value in new_model.model_dump(exclude_defaults=True).items():
        setattr(db_model, field, value)
    await session.commit()
    await session.refresh(db_model)
    return db_model
