import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramAPIError
from aiogram.types import Message, KeyboardButton, ReplyKeyboardMarkup, ErrorEvent
from src.background_task import BackgroundTask
from src.env import BOT_TOKEN
from src.bot_handlers.router import router_handlers

# All handlers should be attached to the Router (or Dispatcher)
dp = Dispatcher()

# Глобальный обработчик ошибок
@dp.error()
async def global_error_handler(event: ErrorEvent):
    """
    Глобальный обработчик ошибок.
    """
    logging.error(f"Ошибка: {event.exception}")

    if isinstance(event.exception, TelegramAPIError):
        logging.error("Ошибка Telegram API")
    else:
        logging.error("Неизвестная ошибка")

    # Если нужно отправить сообщение о проблеме
    if isinstance(event.update.message, Message):
        await event.update.message.reply(f"Произошла ошибка")
    return True  # Не пропускать ошибку дальше

# MAIN
async def main() -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp.include_router(router_handlers)

    task1 = dp.start_polling(bot)
    task2 = BackgroundTask.task_job()
    await asyncio.gather(task2, task1)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())

