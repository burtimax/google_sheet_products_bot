# Создание клавиатуры с кнопками
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Запустить")],
        [KeyboardButton(text="Следующий ключ")],
        [KeyboardButton(text="Стоп")]
    ],
    resize_keyboard=True
)