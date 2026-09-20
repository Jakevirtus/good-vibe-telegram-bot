import asyncio
import os
import random
from aiogram import Bot, Dispatcher, types
from aiogram.client.session.aiohttp import AiohttpSession
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
PROXY_URL = os.getenv("PROXY_URL")

COMPLIMENTS = [
    "Ты сегодня отлично выглядишь! 😎",
    "Твой код становится чище с каждым днем! 💻",
    "У тебя все получится, главное — не сдаваться! 🚀",
    "Ты способен на большее, чем сам думаешь! 🌟",
    "Сегодня отличный день, чтобы узнать что-то новое! 📚",
    "Ты классный программист, даже если сейчас ошибка в коде! 🐛",
    "Твоя усидчивость обязательно приведет к успеху! 🏆"
]

def get_random_compliment():
    return random.choice(COMPLIMENTS)

async def main():
    session = AiohttpSession(proxy=PROXY_URL) if PROXY_URL else None
    bot = Bot(token=BOT_TOKEN, session=session)
    dp = Dispatcher()

    @dp.message()
    async def echo_all(message: types.Message):
        if message.text and message.text.startswith('/start'):
            await message.answer("Привет! Я GoodVibeBot. 😊\nНапиши мне что-нибудь, и я подниму тебе настроение!")
        elif message.text and message.text.startswith('/compliment'):
            await message.answer(get_random_compliment())
        else:
            await message.answer(f"Ты написал: \"{message.text}\"\n\nА вот тебе за это: {get_random_compliment()}")

    print("GoodVibeBot запущен...")
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот остановлен.")
