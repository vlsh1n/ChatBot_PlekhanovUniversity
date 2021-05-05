from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.types import InputFile

from keyboards.default import menu
from keyboards.default import contacts
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


# Обработчик кнопки "Карта кампуса". В ответ присылает карту, которая лежит в директории static, в корне проекта.
@dp.message_handler(text='Карта кампуса')
async def map_of_campus(message: types.Message):
    photo_bytes = InputFile(path_or_bytesio='static/карта-базы.png')
    await message.answer('Присылаю карту')
    await message.answer_photo(photo=photo_bytes)


# Обработчик кнопки "Полезные контакты". В ответ заменяет основную клавиатуру на клавиатуру с выбором отделов.
@dp.message_handler(text='Полезные контакты')
async def general_contacts(message: types.Message):
    await message.answer(text='Выбери нужный отдел', reply_markup=contacts)
