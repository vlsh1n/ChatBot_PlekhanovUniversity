from aiogram import types

from keyboards.default import contacts_prov, contacts_tech, contacts_curators, contacts_press, contacts_sound, menu

from loader import dp


# Обработчик кнопки с категорией Кураторов. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел по работе с участниками')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_curators)


# Обработчик кнопки с категорией Пресса. В ответ присылает список контактов для выбора
@dp.message_handler(text='Пресс центр')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_press)


# Обработчик кнопки с категорией Снабжения. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел планирования и снабжения')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_prov)


# Обработчик кнопки с категорией Техников. В ответ присылает список контактов для выбора
@dp.message_handler(text='Технический отдел')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_tech)


# Обработчик кнопки с категорией Техников. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел аудиовизуального оснащения')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_sound)


# Возвращает пользователя в главное меню
@dp.message_handler(text='В главное меню')
async def back_to_main_menu(message: types.Message):
    await message.answer(text='Вы снова в главном меню', reply_markup=menu)

