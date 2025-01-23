# from aiogram import BaseMiddleware
# from aiogram.exceptions import TelegramAPIError
# from aiogram.types import Message, TelegramObject
# import logging
# from typing import Callable, Dict, Any, Awaitable
#
# class ErrorHandlingMiddleware(BaseMiddleware):
#     """
#     Middleware для глобальной обработки ошибок.
#     """
#
#     async def __call__(
#         self,
#         handler: Callable[[Message, Dict[str, Any]], Awaitable[Any]],
#         event: TelegramObject,
#         data: Dict[str, Any]
#     ) -> Any:
#         try:
#             # Попытка выполнить основной обработчик
#             return await handler(event, data)
#         except TelegramAPIError as e:
#             # Обработка ошибок Telegram API
#             logging.error(f"Ошибка Telegram API: {e}")
#             await event.answer("Произошла ошибка Telegram API. Попробуйте позже.")
#         except Exception as e:
#             # Общая обработка всех остальных ошибок
#             logging.error(f"Неизвестная ошибка: {e}")
#             await event.answer(f"Ошибка: {e}")
#
#         # Важно: если вы возвращаете None, это сигнализирует о том, что событие было обработано.
#         return None
