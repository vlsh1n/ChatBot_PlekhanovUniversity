from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с контактами отдела кураторов
contacts_base = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Беседина Елизавета'),
        KeyboardButton(text='Аникина Таисия'),
        KeyboardButton(text='Шпак Анна')
    ],
    [
        KeyboardButton(text='Деркач Инна'),
        KeyboardButton(text='Кляхина Татьяна'),
        KeyboardButton(text='Кишинек Илья')
    ],
    [
        KeyboardButton(text='Мартиросян Армен'),
        KeyboardButton(text='Гудко Юлия')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])



contacts_school = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Карасиков Евгений')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])
