import json
from random import randint
from aiogram.utils.keyboard import InlineKeyboardBuilder
import ai
from aiogram import types
import dictionaries
from main import database

# Класс скачек
class Racing():
    def __init__(self):
        self.horses = [1, 1, 1]
        self.is_finished = False
        self.winner = None

    async def go(self):
        horse_number = randint(0, 2)
        self.horses[horse_number] += 1
        for horse in self.horses:
            if horse == 5:
                self.is_finished = True
                self.winner = str(self.horses.index(horse) + 1)

    def __str__(self):
        out = ""
        for c, i in enumerate(self.horses):
            out += f"{c+1}. " + "🟩"*i + "\n"
        return out

# Класс крестиков ноликов
class TicTacToe():
    def __init__(self):
        self.board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

    async def place(self, x, y, player):
        self.board[x][y] = player

    async def ai_place(self):
        self.board = ai.TicTacToe(self.board)

    async def check_win(self):
        evaluate = ai.xo.evaluate(self.board)
        return evaluate != 0

    async def check_tie(self):
        for x in self.board:
            for y in x:
                if y == 0:
                    return False
        return True

    async def as_markup(self):
        builder = InlineKeyboardBuilder()
        x_index = 0
        for x in self.board:
            y_index = 0
            for y in x:
                button = types.InlineKeyboardButton(text=await xo_emojinator(y), callback_data=f"xo {x_index}-{y_index}")
                if y_index == 0:
                    builder.row(button)
                else:
                    builder.add(button)
                y_index += 1
            x_index += 1
        return builder.as_markup()

# Преобразование загадок в словарь
async def riddle_dicter(riddle):
    try:
        riddle = riddle.replace("```json", "").replace("```", "")
        new_riddle = json.loads(riddle)
        if set(new_riddle.keys()) == {'question', 'answer'}:
            return new_riddle
        else:
            return None
    except:
        return None

# Я назвал это изобретение эмоджинатор
async def xo_emojinator(number: list[0, 1, 2]):
    match number:
        case 0:
            return "🟪"
        case 1:
            return "🔵"
        case 2:
            return "❌"

# Получить язык
async def get_language(user: types.User):
    db_lang = database.select(["language"], "users", f"id = {user.id}")
    if db_lang:
        if db_lang[0][0]:
            return db_lang[0][0]
    code = user.language_code
    if code in dictionaries.langs:
        return code
    else:
        return "en"

# Чтобы не писать много кода и заменить файл keyboards.py, который раньше был у меня, я создал эту функцию. Она подходит для простеньких кнопок, остальное будет писаться в main.py
async def simple_keyboards(user=None, **buttons):
    builder = InlineKeyboardBuilder()
    for item in buttons.items():
        # Прикол в том, что ключи в словаре написаны с маленькой буквы, а кнопки с заглавной, т.е. конфликта быть не может
        if user != None and item[1] in dictionaries.buttons[await get_language(user)].keys():
            text = dictionaries.buttons[await get_language(user)][item[1]]
        else:
            text = item[1]
        button = types.InlineKeyboardButton(text=text, callback_data=item[0])
        builder.add(button)
    return builder.as_markup()

# Форматирование секунд в дни, часы и минуты (спасибо копилоту)
def format_time(seconds):
    seconds = round(seconds)
    days, seconds = divmod(seconds, 86400)
    hours, seconds = divmod(seconds, 3600)
    minutes, seconds = divmod(seconds, 60)

    result = []
    if days > 0:
        result.append(f"{int(days)} дн")
    if hours > 0:
        result.append(f"{int(hours)} ч")
    if minutes > 0:
        result.append(f"{int(minutes)} мин")
    if seconds > 0:
        result.append(f"{seconds} сек")

    return " ".join(result)
