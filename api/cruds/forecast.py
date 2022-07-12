from sqlalchemy.ext.asyncio import AsyncSession
from typing import List, Tuple, Optional
from sqlalchemy import select
from sqlalchemy.engine import Result
import api.models.forecast as forecast_model
import api.schemas.forecast as forecast_schema


async def create_forecast(
    db: AsyncSession, forecast_create: forecast_schema.ForecastCreate
) -> forecast_model.Forecast:
    forecast = forecast_model.Forecast(**forecast_create.dict())
    db.add(forecast)
    await db.commit()
    await db.refresh(forecast)
    return forecast

async def get_forecasts(db: AsyncSession) -> List[forecast_model.Forecast]:
    result: Result = await db.execute(select(forecast_model.Forecast))
    forecasts: List[Tuple[forecast_model.Forecast]] = result.fetchall()
    return [forecast[0] for forecast in forecasts]

async def get_forecast(db: AsyncSession, forecast_id: int) -> Optional[forecast_model.Forecast]:
    result: Result = await db.execute(
        select(forecast_model.Forecast).filter(forecast_model.Forecast.id == forecast_id)
    )
    forecast: Optional[Tuple[forecast_model.Forecast]] = result.first()
    return forecast[0] if forecast is not None else None  # 要素が一つであってもtupleで返却されるので１つ目の要素を取り出す

async def delete_forecast(db: AsyncSession, original: forecast_model.Forecast) -> None:
    await db.delete(original)
    await db.commit()