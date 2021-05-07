from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

feedback_keyboard_day1 = InlineKeyboardMarkup()
feedback_keyboard_day2 = InlineKeyboardMarkup()
feedback_keyboard_day3 = InlineKeyboardMarkup()
feedback_keyboard_general = InlineKeyboardMarkup()

DAY1_LINK = 'https://forms.gle/nfS6oZ2eWKJsouaVA'
DAY2_LINK = 'https://forms.gle/smYP7HXUMYc1X6dj8'
DAY3_LINK = 'https://forms.gle/xvqeGFrYmzMCRmeT6'
GENERAL_LINK = 'https://forms.gle/7tjMDSJMRqsNSDnVA'

day1 = InlineKeyboardButton(text='Обратная связь: Первый день', url=DAY1_LINK)
day2 = InlineKeyboardButton(text='Обратная связь: Второй день', url=DAY2_LINK)
day3 = InlineKeyboardButton(text='Обратная связь: Третий день', url=DAY3_LINK)
general = InlineKeyboardButton(text='Итоговая обратная связь', url=GENERAL_LINK)

feedback_keyboard_day1.insert(day1)
feedback_keyboard_day2.insert(day2)
feedback_keyboard_day3.insert(day3)
feedback_keyboard_general.insert(general)
