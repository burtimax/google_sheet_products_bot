import asyncio
from src.google_sheet_client import google_sheet_client
from src.ai_clients.chat_gpt_client import ChatGPTClient
from src.notification_service import Notify

is_running = False

class BackgroundTask:

    # Асинхронная задача
    @staticmethod
    async def task_job():
        global is_running
        while True:
            if not is_running:
                await asyncio.sleep(1)
                continue

            data = google_sheet_client.update_data()
            ai = ChatGPTClient()
            i = 1
            while i < len(data.products_info) and is_running:
                try:
                    if (not data.products_info[i].strip()
                            and not data.products_short_info[i].strip()):
                        i += 1
                        continue

                    prod_info = data.products_info[i]
                    if not data.products_info[i].strip():
                        prod_info = data.products_short_info[i]

                    data = google_sheet_client.get_data()


                    print(f"Обработка товара {i}: {prod_info}")
                    #result, prod_ai_desc = ai.get_product_ai_description(data.keys[data.active_key - 1], data.gpt_model, data.prompt, prod_info)
                    result, prod_ai_desc = ai.get_product_ai_description(data.prompt, prod_info)

                    if not result:
                        raise Exception(prod_ai_desc)

                    google_sheet_client.write_product_description(prod_info, prod_ai_desc)
                    print(f"Обработали товар {i}, новое описание: {prod_ai_desc}")

                    if i == 1:
                        google_sheet_client.add_prompt_to_history()
                    await asyncio.sleep(data.timeout_sec)
                    i += 1
                except Exception as e:
                    await Notify(google_sheet_client.get_data().admin_username, str(e))
                    await asyncio.sleep(data.timeout_sec)

            if is_running:
                await BackgroundTask.stop()

    # Функция для запуска планировщика
    @staticmethod
    async def start():
        global is_running
        if not is_running:
            is_running = True
            await Notify(google_sheet_client.get_data().admin_username, "Процесс запустил")
        else:
            await Notify(google_sheet_client.get_data().admin_username, "Процесс уже запущен")

    # Функция для остановки планировщика
    @staticmethod
    async def stop():
        global is_running
        if is_running:
            is_running = False
        await Notify(google_sheet_client.get_data().admin_username, "Процесс завершен")

