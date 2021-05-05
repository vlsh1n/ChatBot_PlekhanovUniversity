from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Расписание'),
        KeyboardButton(text='Полезные контакты')
    ],
    [
        KeyboardButton(text='Правила Школы'),
        KeyboardButton(text='Карта кампуса')
    ],
    [
        KeyboardButton(text='Обратная связь'),
        KeyboardButton(text='Портфолио организаторов')
    ],
    [
        KeyboardButton(text='История Школы Актива'),
        KeyboardButton(text='Книга жалоб и предложений')
    ]
])
