from aiogram import Router, types, html
from services.post_api import get_weather
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command(commands="post"))
async def weather_handler(message: types.Message):
    try:
        weather = await get_weather()
        await message.answer(f"{weather.title}: {weather.id}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
