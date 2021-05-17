from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с выбором отдела контактов
contacts = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Администрация базы'),
        KeyboardButton(text='Администрация Школы Актива')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])
