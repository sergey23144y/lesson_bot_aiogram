from pydantic import BaseModel

class WeatherMain(BaseModel):
  temp: float

class WeatherResponse(BaseModel):
    userId: int
    id: int
    title: str
    body: str