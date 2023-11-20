from pydantic import BaseModel, conint


class SRoadBase(BaseModel):
    id_auto: conint(ge=1)
    road_length: int
    start_point: str
    end_point: str
    id_driver: conint(ge=1)


class SRoad(SRoadBase):
    id_road: conint(ge=1)
