import datetime

from aiogram.types import CallbackQuery, InputFile

from keyboards.inline.callback_data_schedule import day_callback
from loader import dp, bot


# Обработчик инлайн кнопки первого дня в блоке расписание
@dp.callback_query_handler(day_callback.filter(day='first'))
async def day_one(call: CallbackQuery):
    photo_bytes = InputFile(path_or_bytesio='static/schedule/first.jpg')
    if datetime.date.today() >= datetime.date(2021, 5, 18):
        await call.answer(cache_time=60)
        await call.message.answer('Присылаю расписание на первый день')
        await bot.send_photo(chat_id=call.from_user.id, photo=photo_bytes)
    else:
        await call.answer(cache_time=60)
        await call.message.answer(text='Расписание станет доступно 18 мая')


# Обработчик инлайн кнопки второго дня в блоке расписание
@dp.callback_query_handler(day_callback.filter(day='second'))
async def day_two(call: CallbackQuery):
    photo_bytes = InputFile(path_or_bytesio='static/schedule/second.jpg')
    if datetime.date.today() >= datetime.date(2021, 5, 19):
        await call.answer(cache_time=60)
        await call.message.answer('Присылаю расписание на второй день')
        await bot.send_photo(chat_id=call.from_user.id, photo=photo_bytes)
    else:
        await call.answer(cache_time=60)
        await call.message.answer(text='Расписание станет доступно 19 мая')


# Обработчик инлайн кнопки третьего дня в блоке расписание
@dp.callback_query_handler(day_callback.filter(day='third'))
async def day_three(call: CallbackQuery):
    photo_bytes = InputFile(path_or_bytesio='static/schedule/third.jpg')
    if datetime.date.today() >= datetime.date(2021, 5, 20):
        await call.answer(cache_time=60)
        await call.message.answer('Присылаю расписание на третий день')
        await bot.send_photo(chat_id=call.from_user.id, photo=photo_bytes)
    else:
        await call.answer(cache_time=60)
        await call.message.answer(text='Расписание станет доступно 20 мая')


# Обработчик инлайн кнопки четвертого дня в блоке расписание
@dp.callback_query_handler(day_callback.filter(day='fourth'))
async def day_fourth(call: CallbackQuery):
    photo_bytes = InputFile(path_or_bytesio='static/schedule/fourth.jpg')
    if datetime.date.today() >= datetime.date(2021, 5, 21):
        await call.answer(cache_time=60)
        await call.message.answer('Присылаю расписание на четвертый день')
        await bot.send_photo(chat_id=call.from_user.id, photo=photo_bytes)
    else:
        await call.answer(cache_time=60)
        await call.message.answer(text='Расписание станет доступно 21 мая')


# Обработчик инлайн кнопки отмена в блоке расписание, закрывает инлайн клавиатуру
@dp.callback_query_handler(text='cancel')
async def cancel(call: CallbackQuery):
    await call.message.answer('Чем еще могу помочь? :)')
    await call.message.edit_reply_markup()
