from aiogram import types

from aiogram.types import InputFile

from loader import dp, bot


# Список хэндлеров, которые будут ловить нажатия по кнопкам с именами организаторов и возвращать краткую инфу о них

@dp.message_handler(text='Евгений Карасиков')
async def contact(message: types.Message):
    photo = InputFile(path_or_bytesio='static/ProfilePhoto/Карасиков Евгений.jpg')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Карасиков Евгений\n'
                              'Программный директор\n'
                              'Номер телефона: +7(961)590-31-22\n'
                              'Инстаграм: https://instagram.com/karas_i_ko\n'
                              'Вконтакте: https://vk.com/karas_i_ko')

