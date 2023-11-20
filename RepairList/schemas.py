from pydantic import BaseModel, conint


class SRepairListBase(BaseModel):
    id_auto: conint(ge=1)
    time: str
    word: str


class SRepairList(SRepairListBase):
    id_list: conint(ge=1)
