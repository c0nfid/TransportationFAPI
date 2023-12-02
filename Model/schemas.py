from pydantic import BaseModel, conint, ConfigDict


class SModelBase(BaseModel):
    name: str
    vendor_country: str

    model_config = ConfigDict(from_attributes=True)


class SModel(SModelBase):
    id_model: conint(ge=1)


class SUpdateModel(BaseModel):
    name: str | None = None
    vendor_country: str | None = None

    model_config = ConfigDict(from_attributes=True)
