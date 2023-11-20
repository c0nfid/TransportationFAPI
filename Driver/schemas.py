from pydantic import BaseModel, conint


class SDriverBase(BaseModel):
    name: str
    docs: bool


class SDriver(SDriverBase):
    id_driver: conint(ge=1)
