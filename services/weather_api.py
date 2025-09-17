import httpx

from models.weather import WeatherResponse
from config import settings


async def get_weather(city: str) -> WeatherResponse:
  async with httpx.AsyncClient() as client:
    resp = await client.get(
      settings.weather_api_url
    )
    resp.raise_for_status()
    data = resp.json()
    return WeatherResponse(**data)