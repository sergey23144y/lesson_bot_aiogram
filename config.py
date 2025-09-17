from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    bot_token: str
    weather_api_key: str
    weather_api_url: str = "https://jsonplaceholder.typicode.com/posts/1"

    class Config:
        env_file = ".env"

settings = Settings()