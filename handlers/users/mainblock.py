from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from loader import dp


@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите нужную кнопку', reply_markup=menu)
