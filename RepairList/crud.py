from core.base.models import RepairList
from sqlalchemy.ext.asyncio import AsyncSession


async def get_row_by_id(session: AsyncSession, id_row: int) -> RepairList | None:
    return await session.get(RepairList, id_row)
