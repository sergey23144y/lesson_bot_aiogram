import asyncio
from aiogram import Bot, Dispatcher
from config import settings
from handlers import weather


async def main():
    print("settings.bot_token:" + settings.bot_token)
    print("settings.weather_api_key:" + settings.weather_api_key)
    bot = Bot(token=settings.bot_token)
    dp = Dispatcher()

    dp.include_router(weather.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
