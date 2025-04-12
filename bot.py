from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from dotenv import load_dotenv

import os

# Инициализация бота
load_dotenv()
TOKEN = os.getenv("TOKEN")
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()
router = Router()

# Разделение на роутер для тестирования, потому что иногда тестил прямо в чате
white_list = [1223353442]
test_router = Router()
test_router.message.filter(lambda message: message.from_user.id in white_list)
test_router.callback_query.filter(
    lambda callback: callback.from_user.id in white_list)

black_list = []

router.message.filter(lambda message: message.from_user.id not in black_list)
router.callback_query.filter(
    lambda callback: callback.from_user.id not in black_list)