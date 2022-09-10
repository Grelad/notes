import json

from django.shortcuts import render
import asyncio
import aiogram.utils.markdown as md
from aiogram.types import ParseMode
from aiogram import Bot, Dispatcher, types, executor
from first_project import settings

BOT_TOKEN = settings.TG_TOKEN
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

chat_id = 243842517

@dp.message_handler(commands=['start', 'restart'])
async def start_handler(event: types.Message):
    await event.answer(
        f"Hello, {event.from_user.get_mention(as_html=True)} 👋!",
        parse_mode=types.ParseMode.HTML,
    )


async def handler(message: dict):
    await bot.send_message(
        chat_id=chat_id,
        text=md.text(
            md.text('Book name', md.bold(message['name'])),
            md.text('Year of the book:', md.code(message['year'])),
            sep='\n',
        ),
        parse_mode=ParseMode.MARKDOWN,
    )

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
