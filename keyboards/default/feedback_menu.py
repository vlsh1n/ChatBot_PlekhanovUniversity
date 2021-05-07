from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Клавиатура с выбором дня для обратной связи
feedback_menu = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text='Обратная связь: Первый день')
    ],
    [
        KeyboardButton(text='Обратная связь: Второй день')
    ],
    [
        KeyboardButton(text='Обратная связь: Третий день')
    ],
    [
        KeyboardButton(text='Итоговая обратная связь')
    ],
    [
        KeyboardButton(text='В главное меню')
    ]
])