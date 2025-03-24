from aiogram import Bot, Dispatcher, Router
from aiogram.enums import ParseMode
from aiogram.client.bot import DefaultBotProperties

from dotenv import load_dotenv

import os

# Инициализация
load_dotenv()
TOKEN=os.getenv("TOKEN")
bot = Bot(TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()
router = Router()

# штука для тестирования, чтобы никто не мешал тестировать и то, что должно быть реально в боте не перемешивалось с тестами
white_list = [1223353442]
test_router = Router()
test_router.message.filter(lambda message: message.from_user.id in white_list)
test_router.callback_query.filter(lambda callback: callback.from_user.id in white_list)

router.message.filter(lambda message: message.from_user.id in white_list)
router.callback_query.filter(lambda callback: callback.from_user.id in white_list)