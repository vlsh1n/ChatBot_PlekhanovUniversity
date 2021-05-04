from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

schedule = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                            text='День первый',
                                            callback_data='first_day'
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='День второй',
                                            callback_data='second_day'
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='День третий',
                                            callback_data='third_day'
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='Отмена',
                                            callback_data='cancel'
                                        )
                                    ]
                                ])


