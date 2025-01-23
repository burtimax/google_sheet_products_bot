from aiogram import Router
from aiogram.types import Message
from .keyboards import keyboard
from src.background_task import BackgroundTask
from src.google_sheet_client import google_sheet_client

router_handlers = Router()
#router_handlers.message.middleware(ErrorHandlingMiddleware)
bg_task = BackgroundTask()

def user_authorized(message: Message) -> bool:
    return google_sheet_client.get_data().admin_username.endswith(message.from_user.username) \
    or str(message.chat.id) == google_sheet_client.get_data().admin_username

@router_handlers.message(lambda message: message.text.startswith("/start"))
async def send_welcome(message: Message):
    google_sheet_client.update_data()

    if user_authorized(message) == False and user_authorized(message) == False:
        return await default_handler(message)

    data = google_sheet_client.get_data()
    if data.admin_username.isnumeric() == False:
        data.admin_username = message.chat.id
        google_sheet_client.set_data(data)

    await message.answer(
        "Заполните таблицу и нажмите кнопку Запустить",
        reply_markup=keyboard
    )

@router_handlers.message(lambda message: message.text == "Запустить" and (user_authorized(message)))
async def handle_start_button(message: Message):
    await message.answer(
        "Вы нажали кнопку 'Запустить'. Запускаю процесс...",
        reply_markup=keyboard
    )
    # Здесь можно добавить логику для запуска процесса
    await BackgroundTask.start()


# Обработчик кнопки "Следующий ключ"
@router_handlers.message(lambda message: message.text == "Следующий ключ" and (user_authorized(message)))
async def handle_next_key_button(message: Message):
    # Здесь можно добавить логику для перехода к следующему ключу
    data = google_sheet_client.get_data()
    key_index = data.active_key
    key_index = (key_index + 1) % (len(data.keys) + 1)
    data.active_key = 1 if key_index==0 else key_index
    google_sheet_client.set_data(data)

    await message.answer(
        f"Следующий ключ установлен [№ {data.active_key}]",
        reply_markup=keyboard
    )

# Обработчик кнопки "Стоп"
@router_handlers.message(lambda message: message.text == "Стоп" and (user_authorized(message)))
async def handle_stop_button(message: Message):
    await message.answer(
        "Вы нажали кнопку 'Стоп'. Процесс останавливается.",
        reply_markup=keyboard
    )
    # Здесь можно добавить логику для остановки процесса
    await BackgroundTask.stop()

@router_handlers.message()
async def default_handler(message: Message):
    await message.answer(
        "Не знаю ничего.",
        reply_markup=keyboard
    )