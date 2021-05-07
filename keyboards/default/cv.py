from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с выбором отдела контактов
cv = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отдел по работе с участниками CV'),
        KeyboardButton(text='Пресс центр CV')
    ],
    [
        KeyboardButton(text='Отдел планирования и снабжения CV'),
        KeyboardButton(text='Технический отдел CV')
    ],
    [
        KeyboardButton(text='Отдел аудиовизуального оснащения CV')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])