from core.base.models import Model
from sqlalchemy.ext.asyncio import AsyncSession


async def get_model_by_id(session: AsyncSession, model_id: int) -> Model | None:
    return await session.get(Model, model_id)
