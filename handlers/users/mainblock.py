from aiogram import types
from aiogram.dispatcher.filters import Command

from keyboards.default import menu
from keyboards.inline.schedule import schedule
from loader import dp


# При отправке команды /menu, вызывается меню с выбором функций
@dp.message_handler(Command('menu'))
async def show_menu(message: types.Message):
    await message.answer('Выберите нужную кнопку', reply_markup=menu)


# Обработчик кнопки "Расписание". В ответ присылает сообщение с просьбой выбрать нужный день и инлайн клавиатуру для
# перехода по соответствующим дням
@dp.message_handler(text='Расписание')
async def main_schedule(message: types.Message):
    await message.answer(text='Выбери нужный день', reply_markup=schedule)
