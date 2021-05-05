from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from keyboards.inline.callback_data_schedule import day_callback

schedule = InlineKeyboardMarkup(row_width=1,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(
                                            text='День первый',
                                            callback_data=day_callback.new(day='first')
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='День второй',
                                            callback_data='schedule:second'
                                        )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='День третий',
                                            callback_data='schedule:third'
                                        )
                                    ],
                                    [
                                      InlineKeyboardButton(
                                          text='День четвертый',
                                          callback_data='schedule:fourth'
                                      )
                                    ],
                                    [
                                        InlineKeyboardButton(
                                            text='Отмена',
                                            callback_data='cancel'
                                        )
                                    ]
                                ])


