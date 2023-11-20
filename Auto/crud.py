from sqlalchemy.ext.asyncio import AsyncSession
from core.base.models import Auto
from Auto.schemas import SAutoModels, SAuto, SAutoWithModel


async def get_auto_by_id(session: AsyncSession, auto_id: int) -> Auto | None:
    return await session.get(Auto, auto_id)


async def join_table(autos: list | None, order: str, jnt: bool):
    result_autos = []
    for auto in autos:
        response = SAutoModels(**auto.__dict__)
        #response = SAutoWithModel(**auto.__dict__)
        auto = response.model_dump()
        auto.update(auto["model"])
        del auto["model"]
        result_autos.append(auto)
    if jnt:
        result_autos = sorted(result_autos, key=lambda d: d[order])
    return result_autos
