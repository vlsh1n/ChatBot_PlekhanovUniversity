import datetime

from aiogram import types

from keyboards.inline.feedback import feedback_keyboard_day1, feedback_keyboard_day2, feedback_keyboard_day3, \
    feedback_keyboard_general
from keyboards.default import menu

from loader import dp


# Обработчик кнопки обратной связи первого дня,
# при запросе не раньше указаной даты, в ответ присылает ссылку на гугл форму
@dp.message_handler(text='Обратная связь: Первый день')
async def feedback_day_one(message: types.Message):
    if datetime.date.today() >= datetime.date(2021, 5, 19):
        await message.answer(text='Перейди по ссылке ниже, чтобы оставить обратную связь',
                             reply_markup=feedback_keyboard_day1)
    else:
        await message.answer(text='Обратная связь по первому дню станет доступна 20 мая')


# Обработчик кнопки обратной связи второго дня,
# при запросе не раньше указаной даты, в ответ присылает ссылку на гугл форму
@dp.message_handler(text='Обратная связь: Второй день')
async def feedback_day_two(message: types.Message):
    if datetime.date.today() >= datetime.date(2021, 5, 20):
        await message.answer(text='Перейди по ссылке ниже, чтобы оставить обратную связь',
                             reply_markup=feedback_keyboard_day2)
    else:
        await message.answer(text='Обратная связь по второму дню станет доступна 21 мая')


# Обработчик кнопки обратной связи третьего дня,
# при запросе не раньше указаной даты, в ответ присылает ссылку на гугл форму
@dp.message_handler(text='Обратная связь: Третий день')
async def feedback_day_three(message: types.Message):
    if datetime.date.today() >= datetime.date(2021, 5, 21):
        await message.answer(text='Перейди по ссылке ниже, чтобы оставить обратную связь',
                             reply_markup=feedback_keyboard_day3)
    else:
        await message.answer(text='Обратная связь по третьему дню станет доступна 22 мая')


# Обработчик кнопки общей обратной связи, при запросе не раньше указаной даты, в ответ присылает ссылку на гугл форму
@dp.message_handler(text='Итоговая обратная связь')
async def feedback_general(message: types.Message):
    if datetime.date.today() >= datetime.date(2021, 5, 21):
        await message.answer(text='Перейди по ссылке ниже, чтобы оставить обратную связь',
                             reply_markup=feedback_keyboard_general)
    else:
        await message.answer(text='Итоговая обратная связь станет доступна 23 мая')


# Возвращает пользователя в главное меню
@dp.message_handler(text='В главное меню')
async def back_to_main_menu(message: types.Message):
    await message.answer(text='Вы снова в главном меню', reply_markup=menu)
