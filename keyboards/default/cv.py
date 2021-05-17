from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с выбором отдела контактов
cv = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отдел по работе с участниками'),
        KeyboardButton(text='Пресс центр')
    ],
    [
        KeyboardButton(text='Отдел планирования и снабжения'),
        KeyboardButton(text='Технический отдел')
    ],
    [
        KeyboardButton(text='Отдел аудиовизуального оснащения')
    ],
    [
        KeyboardButton(text='Евгений Карасиков')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])