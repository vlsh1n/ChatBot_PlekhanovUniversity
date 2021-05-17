from aiogram import types

from keyboards.default import cv_prov, cv_tech, cv_sound, cv_press, cv_curators

from loader import dp


# Обработчик кнопки с категорией Кураторов. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел по работе с участниками ')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=cv_curators)


# Обработчик кнопки с категорией Пресса. В ответ присылает список контактов для выбора
@dp.message_handler(text='Пресс центр ')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=cv_press)


# Обработчик кнопки с категорией Снабжения. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел планирования и снабжения ')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=cv_prov)


# Обработчик кнопки с категорией Техников. В ответ присылает список контактов для выбора
@dp.message_handler(text='Технический отдел ')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=cv_tech)


# Обработчик кнопки с категорией Звукарей. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел аудиовизуального оснащения ')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=cv_sound)
