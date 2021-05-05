from aiogram import types

from keyboards.default import contacts_prov, contacts_tech, contacts_curators, contacts_press, menu

from loader import dp


# Обработчик кнопки с категорией Кураторов. В ответ присылает список контактов для выбора
@dp.message_handler(text='Отдел по работе с участниками')
async def category_curators(message: types.Message):
    await message.answer(text='Выбери нужный контакт', reply_markup=contacts_curators)


# Возвращает пользователя в главное меню
@dp.message_handler(text='В главное меню')
async def back_to_main_menu(message: types.Message):
    await message.answer(text='Вы снова в главном меню', reply_markup=menu)

