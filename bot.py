import asyncio
import os
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("BOT_TOKEN")  # Render'dan olinadi

bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def reply_to_all(message: types.Message):
    await message.answer("Assalomu alaykum ,\nMurojaatingiz ko‘rib chiqilmoqda ✅")

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
