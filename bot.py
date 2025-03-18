from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from dotenv import load_dotenv
import os


load_dotenv()
TOKEN=os.getenv("TOKEN")
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()
