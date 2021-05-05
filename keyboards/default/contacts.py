from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с выбором отдела контактов
contacts = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Отдел по работе с участниками'),
        KeyboardButton(text='Пресс центр')
    ],
    [
        KeyboardButton(text='Отдел снабжения'),
        KeyboardButton(text='Технический отдел')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])
