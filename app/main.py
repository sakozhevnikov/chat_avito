import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from app.core.config import settings
from app.bot.orchestrator import process_message

# Поменяй на свой смешанный порт из Hiddify
MIXED_PORT = 12334

session = AiohttpSession(proxy=f"http://127.0.0.1:{MIXED_PORT}")
bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, session=session)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    reply = await process_message(str(message.chat.id), message.text)
    await message.answer(reply)

async def main():
    print(f"Бот запущен через Hiddify (порт {MIXED_PORT})...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())