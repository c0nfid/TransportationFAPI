from core.base.models import Driver
from sqlalchemy.ext.asyncio import AsyncSession


async def get_driver_by_id(session: AsyncSession, id_driver: int) -> Driver | None:
    return await session.get(Driver, id_driver)
