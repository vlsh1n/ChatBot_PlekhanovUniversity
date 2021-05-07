from aiogram import types

from aiogram.types import InputFile

from loader import dp, bot


@dp.message_handler(text='Волошин Владислав CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Волошин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Беседина Елизавета CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Беседина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Аникина Таисия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Аникина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Шпак Анна CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Шпак.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Деркач Инна CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Деркач-Инна.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Кляхина Татьяна CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Кляхина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Кишинек Илья CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Кишинек.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Мартиросян Армен CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Мартиросян.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Гудко Юлия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Гудко.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Самохин Андрей CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Самохин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Саркисян Нарек CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Саркисян.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Турк Тимур CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Турк.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Бацман Анастасия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Бацман.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Колесник Алина CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Колесник.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Калашникова Валерия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Калашникова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Мельникова Соня CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Мельникова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Деркач Анастасия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Деркач-Настя.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Стратон Екатерина CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Стратон.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Третьякова Эля CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Третьякова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Ефанова Юлия CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Ефанова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Ковалева Алена CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Ковалева.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Голяндин Даниил CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Голяндин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)


@dp.message_handler(text='Хорин Виталий CV')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Хорин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
