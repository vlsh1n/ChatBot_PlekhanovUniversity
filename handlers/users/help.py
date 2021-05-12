from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


# Хэндлер, который присылает, список команд, которые можно использовать в боте на команду /help
@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = ("Список команд: ",
            "/start - Начать диалог",
            "/help - Получить справку",
            "/menu - Открыть главное меню")
    
    await message.answer("\n".join(text))
