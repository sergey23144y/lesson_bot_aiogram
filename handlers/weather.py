from aiogram import Router, types, html
from services.weather_api import get_weather
from aiogram.filters import CommandStart, Command

router = Router()


@router.message(CommandStart())
async def command_start_handler(message: types.Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!")


@router.message(Command(commands="help"))
async def weather_handler(message: types.Message):
    parts = message.text.split(maxsplit=1)
    if len(parts) < 2:
        await message.answer("Напиши город: /weather Москва")
        return
    city = parts[1]
    try:
        weather = await get_weather(city)
        await message.answer(f"{weather.title}: {weather.id}°C")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")
