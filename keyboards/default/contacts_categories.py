from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с контактами отдела кураторов
contacts_curators = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='test'),
        KeyboardButton(text='test'),
        KeyboardButton(text='test')
    ],
    [
        KeyboardButton(text='test'),
        KeyboardButton(text='test'),
        KeyboardButton(text='test')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

contacts_press = None

contacts_prov = None

contacts_tech = None
