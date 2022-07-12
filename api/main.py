from fastapi import FastAPI
from api.routers import forecast

app = FastAPI()


app = FastAPI()
app.include_router(forecast.router)