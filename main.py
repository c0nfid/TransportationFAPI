from fastapi import FastAPI, Depends, status, HTTPException
from Model.views import router as models_router
from Auto.views import router as autos_router
from Driver.views import router as drivers_router
from RepairList import router as repairs_router
from Road import router as roads_router
from fastapi.middleware.cors import CORSMiddleware

from core.config import settings

app = FastAPI(title="Грузоперевозки Казахстан")
app.include_router(models_router)
app.include_router(autos_router)
app.include_router(drivers_router)
app.include_router(repairs_router)
app.include_router(roads_router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
