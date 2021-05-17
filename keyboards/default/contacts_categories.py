from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с контактами отдела кураторов
contacts_base = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Директор базы')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])


contacts_school = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Начальник отдела благоустройства базы'),
        KeyboardButton(text='Начальник отдела работы с участниками')
    ],
    [
        KeyboardButton(text='Программный директор')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])
