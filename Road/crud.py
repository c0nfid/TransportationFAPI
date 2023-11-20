from core.base.models import Road
from sqlalchemy.ext.asyncio import AsyncSession


async def get_road_by_id(session: AsyncSession, id_road: int) -> Road | None:
    return await session.get(Road, id_road)
