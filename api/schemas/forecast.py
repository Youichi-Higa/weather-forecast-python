from typing import Union
from pydantic import BaseModel, Field

class ForecastBase(BaseModel):
    city: str = Field(None, example="東京")
    public_time: str = Field(None, example="2021/03/03 05:00:00")
    day1_date: str = Field(None, example="2021-03-03")
    day1_image_url: str = Field(None, example="https://www.jma.go.jp/bosai/forecast/img/100.svg")
    day1_telop: str = Field(None, example="晴れ")
    day1_max_temp: Union[str, None] = Field(None, example="19")
    day1_min_temp: Union[str, None] = Field(None, example="5")
    day2_date: str = Field(None, example="2021-03-04")
    day2_image_url: str = Field(None, example="https://www.jma.go.jp/bosai/forecast/img/212.svg")
    day2_telop: str = Field(None, example="曇のち一時雨")
    day2_max_temp: Union[str, None] = Field(None, example="18")
    day2_min_temp: Union[str, None] = Field(None, example="4")
    day3_date: str = Field(None, example="2021-03-05")
    day3_image_url: str = Field(None, example="https://www.jma.go.jp/bosai/forecast/img/313.svg")
    day3_telop: str = Field(None, example="雨のち曇")
    day3_max_temp: Union[str, None] = Field(None, example="20")
    day3_min_temp: Union[str, None] = Field(None, example="10")

class ForecastCreate(ForecastBase):
    pass

class ForecastCreateResponse(ForecastCreate):
    id: int

    class Config:
        orm_mode = True

class Forecast(ForecastBase):
    id: int

    class Config:
        orm_mode = True
