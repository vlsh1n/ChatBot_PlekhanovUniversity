from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp


# Эхо хендлер, куда летят текстовые сообщения, которые не обрабатываются ни одним из других хэндлеров
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):
    await message.answer(f"Сообщение:\n"
                         f"{message.text}")