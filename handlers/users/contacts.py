from aiogram import types

from aiogram.types import InputFile

from loader import dp, bot


# Список хэндлеров, которые будут ловить нажатия по кнопкам с именами организаторов и возвращать краткую инфу о них

@dp.message_handler(text='Программный директор')
async def contact(message: types.Message):
    photo = InputFile(path_or_bytesio='static/ProfilePhoto/Карасиков Евгений.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Карасиков Евгений\n'
                              'Программный директор\n'
                              'Номер телефона: +7(961)590-31-22\n'
                              'Инстаграм: https://instagram.com/karas_i_ko\n'
                              'Вконтакте: https://vk.com/karas_i_ko')


@dp.message_handler(text='Директор базы')
async def contact(message: types.Message):
    await message.answer(text='Баланда Евгений Михайлович\n'
                              'Директор базы\n'
                              'Номер телефона: +7(918)399-01-21\n')


@dp.message_handler(text='Начальник отдела благоустройства базы')
async def contact(message: types.Message):
    photo = InputFile(path_or_bytesio='static/ProfilePhoto/Третьякова Эля.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Третьякова Эля\n'
                              'Начальник отдела благоустройства базы\n'
                              'Номер телефона: +7(918)934-98-51\n'
                              'Инстаграм: https://www.instagram.com/elya__tr/\n'
                              'Вконтакте: https://vk.com/elya_tr')


@dp.message_handler(text='Начальник отдела работы с участниками')
async def contact(message: types.Message):
    photo = InputFile(path_or_bytesio='static/ProfilePhoto/Беседина Елизавета.jpeg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Беседина Елизавета\n'
                              'Руководитель отдела Кураторов\n'
                              'Номер телефона: +7(905)470-60-26\n'
                              'Инстаграм: https://instagram.com/_elizzaa.__\n'
                              'Вконтакте: https://vk.com/id327156342')
