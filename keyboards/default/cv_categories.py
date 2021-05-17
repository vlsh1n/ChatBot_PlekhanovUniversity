from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с контактами отдела кураторов
cv_curators = ReplyKeyboardMarkup(keyboard=[
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

cv_press = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Бацман Анастасия'),
        KeyboardButton(text='Волошин Владислав'),
        KeyboardButton(text='Колесник Алина')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_prov = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Калашникова Валерия'),
        KeyboardButton(text='Мельникова Соня')
    ],
    [
        KeyboardButton(text='Деркач Анастасия'),
        KeyboardButton(text='Стратон Екатерина')
    ],
    [
        KeyboardButton(text='Третьякова Эля'),
        KeyboardButton(text='Ефанова Юлия')
    ],
    [
        KeyboardButton(text='Ковалева Алена')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_tech = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Самохин Андрей'),
        KeyboardButton(text='Саркисян Нарек'),
        KeyboardButton(text='Турк Тимур')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])

cv_sound = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Хорин Виталий')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])