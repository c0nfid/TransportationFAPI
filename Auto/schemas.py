from pydantic import BaseModel, conint, ConfigDict
from Model.schemas import SModel


class SAutoBase(BaseModel):
    id_model: conint(ge=1)
    capacity: int
    docs: bool


class SAuto(SAutoBase):
    id_auto: conint(ge=1)


class SAutoWithModel(SAuto):
    name: str
    vendor_country: str


class SAutoModels(SAuto):
    model: SModel

    model_config = ConfigDict(from_attributes=True)
