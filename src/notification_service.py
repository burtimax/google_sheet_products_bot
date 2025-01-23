import asyncio
from aiogram import Bot
from src.env import BOT_TOKEN


async def Notify(chat_id, text):
    async with Bot(BOT_TOKEN) as bot:
        await bot.send_message(chat_id, text=text)
