from aiogram import types

from keyboards.default import contacts_school, contacts_base

from loader import dp


@dp.message_handler(text='Администрация базы')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_base)


@dp.message_handler(text='Администрация школы')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_school)
