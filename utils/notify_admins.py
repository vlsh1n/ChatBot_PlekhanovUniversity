import logging

from aiogram import Dispatcher

from data.config import ADMINS


# Функция, которая информирует админов о запуске бота
async def on_startup_notify(dp: Dispatcher):
    for admin in ADMINS:
        try:
            await dp.bot.send_message(admin, "Бот Запущен")

        except Exception as err:
            logging.exception(err)
