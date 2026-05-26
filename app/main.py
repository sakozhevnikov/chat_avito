import asyncio
from aiogram import Bot, Dispatcher, types
from app.core.config import settings
from app.bot.orchestrator import process_message
from app.db.session import init_db

bot = Bot(token=settings.TELEGRAM_BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    reply = await process_message(str(message.chat.id), message.text)
    await message.answer(reply)

async def main():
    # Создаём таблицы в БД (если ещё не созданы)
    # await init_db()  # временно отключено, пока не настроим PostgreSQL
    print("Бот запущен...")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())