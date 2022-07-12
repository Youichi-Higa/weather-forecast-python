from sqlalchemy import Column, Integer, String
from api.db import Base


class Forecast(Base):
    __tablename__ = "forecasts"

    id = Column(Integer, primary_key=True)
    city = Column(String(50), nullable=False)
    public_time = Column(String(50), nullable=False)
    day1_date = Column(String(50), nullable=False)
    day1_image_url = Column(String(1024), nullable=False)
    day1_telop = Column(String(50), nullable=False)
    day1_max_temp = Column(String(50), nullable=True)
    day1_min_temp = Column(String(50), nullable=True)
    day2_date = Column(String(50), nullable=False)
    day2_image_url = Column(String(1024), nullable=False)
    day2_telop = Column(String(50), nullable=False)
    day2_max_temp = Column(String(50), nullable=True)
    day2_min_temp = Column(String(50), nullable=True)
    day3_date = Column(String(50), nullable=False)
    day3_image_url = Column(String(1024), nullable=False)
    day3_telop = Column(String(50), nullable=False)
    day3_max_temp = Column(String(50), nullable=True)
    day3_min_temp = Column(String(50), nullable=True)
