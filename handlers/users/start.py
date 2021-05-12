from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp


# Хэндлер, который обрабатывает команду /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Я - чатбот VIII Школы Актива РЭУ им. Г.В.Плеханова!\n"
                         f"У меня ты сможешь узнать всю необходимую информацию, касаемо Школы Актива!")
    await message.answer('Выберите нужную кнопку', reply_markup=menu)

