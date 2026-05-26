import asyncio
from aiogram import Bot
from app.core.config import settings
from app.messenger.base import MessengerAdapter

class TelegramAdapter(MessengerAdapter):
    def __init__(self):
        self.bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)

    async def send_message(self, chat_id: str, text: str) -> None:
        await self.bot.send_message(chat_id=chat_id, text=text)