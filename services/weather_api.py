import httpx

from models.post import PostResponse
from config import settings


async def get_weather() -> PostResponse:
  async with httpx.AsyncClient() as client:
    resp = await client.get(
      settings.weather_api_url
    )
    resp.raise_for_status()
    data = resp.json()
    return PostResponse(**data)
