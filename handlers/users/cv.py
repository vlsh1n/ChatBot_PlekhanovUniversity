from aiogram import types

from aiogram.types import InputFile

from loader import dp, bot


# Список хэндлеров, который ловит нажатия по оргам из меню портфолио организаторов. В ответ присылает постер на орга

@dp.message_handler(text='Волошин Владислав')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Волошин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Волошин Владислав\n'
                              'Разработчик телеграм-канала / Видеограф\n'
                              'Номер телефона: +7(918)042-62-82\n'
                              'Инстаграм: instagram.com/vlsh1n\n'
                              'Вконтакте: vk.com/vlsh1n')


@dp.message_handler(text='Беседина Елизавета')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Беседина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Беседина Елизавета\n'
                              'Руководитель отдела Кураторов\n'
                              'Номер телефона: +7(905)470-60-26\n'
                              'Инстаграм: https://instagram.com/_elizzaa.__\n'
                              'Вконтакте: https://vk.com/id327156342')


@dp.message_handler(text='Аникина Таисия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Аникина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Аникина Таисия\n'
                              'Старший куратор\n'
                              'Номер телефона: +7(918)686-71-78\n'
                              'Инстаграм: instagram.com/taya_burton\n'
                              'Вконтакте: http://vk.com/taya_burton')


@dp.message_handler(text='Шпак Анна')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Шпак.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Шпак Анна\n'
                              'Куратор / Хореограф\n'
                              'Номер телефона: +7(928)847-04-47\n'
                              'Инстаграм: https://instagram.com/_aana_aana_\n'
                              'Вконтакте: https://vk.com/anya_hp')


@dp.message_handler(text='Деркач Инна')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Деркач-Инна.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Деркач Инна\n'
                              'Куратор\n'
                              'Номер телефона: +7(999)637-22-60\n'
                              'Инстаграм: https://instagram.com/innochkaderkach\n'
                              'Вконтакте: https://vk.com/id153602793')


@dp.message_handler(text='Кляхина Татьяна')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Кляхина.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Кляхина Татьяна\n'
                              'Куратор\n'
                              'Номер телефона: +7(918)231-96-01\n'
                              'Инстаграм: https://www.instagram.com/tataperova/\n'
                              'Вконтакте: http://vk.com/tataperova')


@dp.message_handler(text='Кишинек Илья')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Кишинек.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Кишинек Илья\n'
                              'Куратор\n'
                              'Номер телефона: +7(918)687-05-81\n'
                              'Инстаграм: instagram.com/_kishinek_\n'
                              'Вконтакте: vk.com/kishinek')


@dp.message_handler(text='Мартиросян Армен')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Мартиросян.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Мартиросян Армен\n'
                              'Куратор\n'
                              'Номер телефона: +7(918)652-22-27\n'
                              'Инстаграм: instagram.com/armen_mart07\n'
                              'Вконтакте: http://vk.com/armen_mart07')


@dp.message_handler(text='Гудко Юлия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Гудко.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Гудко Юлия\n'
                              'Куратор\n'
                              'Номер телефона: +7(913)876-71-61\n'
                              'Инстаграм: https://instagram.com/_gudok\n'
                              'Вконтакте: https://vk.com/ygudko1')


@dp.message_handler(text='Самохин Андрей')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Самохин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Самохин Андрей\n'
                              'Игротехник\n'
                              'Номер телефона: +7(988)142-25-35\n'
                              'Инстаграм: https://instagram.com/sovetovandrey\n'
                              'Вконтакте: https://vk.com/druidikk')


@dp.message_handler(text='Саркисян Нарек')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Саркисян.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Саркисян Нарек \n'
                              'Игротехник\n'
                              'Номер телефона: +7(918)480-02-07\n'
                              'Инстаграм: instagram.com/nsarkisyan20\n'
                              'Вконтакте: vk.com/brow_lex')


@dp.message_handler(text='Турк Тимур')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Турк.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Турк Тимур\n'
                              'Игротехник\n'
                              'Номер телефона: +7(988)474-31-89\n'
                              'Инстаграм: instagram.com/lll_wassup_lll\n'
                              'Вконтакте: vk.com/l_wassup_l')


@dp.message_handler(text='Бацман Анастасия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Бацман.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Бацман Анастасия\n'
                              'Руководитель пресс-центра / Видеограф\n'
                              'Номер телефона: +7(989)814-52-12\n'
                              'Инстаграм: instagram.com/_tvoya_asya_\n'
                              'Вконтакте: vk.com/tvoya_asyaa')


@dp.message_handler(text='Колесник Алина')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Колесник.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Колесник Алина\n'
                              'Фотограф\n'
                              'Номер телефона: +7(999)638-74-03\n'
                              'Инстаграм: https://instagram.com/alina_kolesnik_\n'
                              'Вконтакте: http://vk.com/id146438297')


@dp.message_handler(text='Калашникова Валерия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Калашникова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Калашникова Валерия\n'
                              'Руководитель О.П.С / Королева Штаба\n'
                              'Номер телефона: +7(908)691-98-53\n'
                              'Инстаграм: https://instagram.com/latte_0.o_\n'
                              'Вконтакте: https://vk.com/id573296097')


@dp.message_handler(text='Мельникова Соня')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Мельникова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Мельникова Соня\n'
                              'Администратор по площадкам\n'
                              'Номер телефона: +7(918)932-98-25\n'
                              'Инстаграм: instagram.com/veseliimelnik\n'
                              'Вконтакте: https://vk.com/id324846942')


@dp.message_handler(text='Деркач Анастасия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Деркач-Настя.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Деркач Анастасия\n'
                              'Администратор по площадкам\n'
                              'Номер телефона: +7(989)815-68-86\n'
                              'Инстаграм: https://instagram.com/nastya64_\n'
                              'Вконтакте: https://vk.com/id282943208')


@dp.message_handler(text='Стратон Екатерина')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Стратон.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Стратон Екатерина\n'
                              'Администратор по площадкам / Хореограф\n'
                              'Номер телефона: +7(918)098-16-26\n'
                              'Инстаграм: https://www.instagram.com/stratosha/\n'
                              'Вконтакте: https://vk.com/k.stratosha')


@dp.message_handler(text='Третьякова Эля')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Третьякова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Третьякова Эля\n'
                              'Ответственная за соц-бытовые вопросы\n'
                              'Номер телефона: +7(918)934-98-51\n'
                              'Инстаграм: https://www.instagram.com/elya__tr/\n'
                              'Вконтакте: https://vk.com/elya_tr')


@dp.message_handler(text='Ефанова Юлия')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Ефанова.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Ефанова Юлия\n'
                              'Администратор по площадкам\n'
                              'Номер телефона: +7(918)367-49-15\n'
                              'Инстаграм: https://instagram.com/efanova_julia\n'
                              'Вконтакте: https://vk.com/id43614184')


@dp.message_handler(text='Ковалева Алена')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Ковалева.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Ковалева Алена\n'
                              'Администратор по площадкам\n'
                              'Номер телефона: +7(918)023-75-50\n'
                              'Инстаграм: https://instagram.com/al.kv\n'
                              'Вконтакте: http://vk.com/alkovaleva23')


@dp.message_handler(text='Хорин Виталий')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Хорин.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Хорин Виталий\n'
                              'Звукорежиссер\n'
                              'Номер телефона: +7(918)947-52-12\n'
                              'Инстаграм: https://instagram.com/vitaliy.horin\n'
                              'Вконтакте: https://vk.com/v_horin')


@dp.message_handler(text='Евгений Карасиков')
async def cv_orgs(message: types.Message):
    photo = InputFile(path_or_bytesio='static/cv/Карасиков.png')
    await bot.send_photo(chat_id=message.from_user.id, photo=photo)
    await message.answer(text='Карасиков Евгений\n'
                              'Программный директор\n'
                              'Номер телефона: +7(961)590-31-22\n'
                              'Инстаграм: https://instagram.com/karas_i_ko\n'
                              'Вконтакте: https://vk.com/karas_i_ko')
