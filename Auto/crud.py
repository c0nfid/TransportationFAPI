from sqlalchemy.ext.asyncio import AsyncSession
from core.base.models import Auto
from Auto.schemas import SAutoModels, SAuto, SAutoWithModel


async def get_auto_by_id(session: AsyncSession, auto_id: int) -> Auto | None:
    return await session.get(Auto, auto_id)


async def merge_auto_with_model(autos: list | None):
    result_autos = []
    for auto in autos:
        model = SAuto(**auto["Auto"].__dict__)
        model.model_dump()
        print(model)
        result_autos.append(auto)

    return result_autos
