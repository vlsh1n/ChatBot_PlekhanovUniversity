from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с контактами отдела кураторов
cv_curators = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Беседина Елизавета CV'),
        KeyboardButton(text='Аникина Таисия CV'),
        KeyboardButton(text='Шпак Анна CV')
    ],
    [
        KeyboardButton(text='Деркач Инна CV'),
        KeyboardButton(text='Кляхина Татьяна CV'),
        KeyboardButton(text='Кишинек Илья CV')
    ],
    [
        KeyboardButton(text='Мартиросян Армен CV'),
        KeyboardButton(text='Гудко Юлия CV')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_press = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Бацман Анастасия CV'),
        KeyboardButton(text='Волошин Владислав CV'),
        KeyboardButton(text='Колесник Алина CV')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_prov = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Калашникова Валерия CV'),
        KeyboardButton(text='Мельникова Соня CV')
    ],
    [
        KeyboardButton(text='Деркач Анастасия CV'),
        KeyboardButton(text='Стратон Екатерина CV')
    ],
    [
        KeyboardButton(text='Третьякова Эля CV'),
        KeyboardButton(text='Ефанова Юлия CV')
    ],
    [
        KeyboardButton(text='Ковалева Алена CV')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_tech = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Самохин Андрей CV'),
        KeyboardButton(text='Саркисян Нарек CV'),
        KeyboardButton(text='Турк Тимур CV')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_sound = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Голяндин Даниил CV'),
        KeyboardButton(text='Хорин Виталий CV'),
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])