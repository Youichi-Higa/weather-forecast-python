from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List
import api.schemas.forecast as forecast_schema
import api.cruds.forecast as forecast_crud
from api.db import get_db

router = APIRouter()


@router.get("/forecasts", response_model=List[forecast_schema.Forecast])
async def list_forecasts(db: AsyncSession = Depends(get_db)):
    return await forecast_crud.get_forecasts(db)

@router.post("/forecasts", response_model=forecast_schema.ForecastCreateResponse)
async def create_forecast(
    forecast_body: forecast_schema.ForecastCreate, db: AsyncSession = Depends(get_db)
):
    return await forecast_crud.create_forecast(db, forecast_body)

@router.delete("/forecasts/{forecast_id}", response_model=None)
async def delete_forecast(forecast_id: int, db: AsyncSession = Depends(get_db)):
    forecast = await forecast_crud.get_forecast(db, forecast_id=forecast_id)
    if forecast is None:
        raise HTTPException(status_code=404, detail="Forecast not found")

    return await forecast_crud.delete_forecast(db, original=forecast)