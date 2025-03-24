import json
from random import randint
from aiogram.utils.keyboard import InlineKeyboardBuilder
import ai
from aiogram import types
import languages

class Racing():
    def __init__(self):
        self.horses = [1, 1, 1, 1]
        self.is_finished = False
        self.winner = None
    
    async def go(self):
        horse_number = randint(0, 3)
        self.horses[horse_number] += 1
        for horse in self.horses:
            if horse == 5:
                self.is_finished = True
                self.winner = self.horses.index(horse) + 1


    def __str__(self):
        out = ""
        for c, i in enumerate(self.horses):
            out +=  f"{c+1}. " + "🟩"*i + "\n"
        return out
    
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

async def riddle_dicter(riddle):
    try:
        riddle  = riddle.replace("```json", "").replace("```", "")
        new_riddle = json.loads(riddle)
        if set(new_riddle.keys()) == {'question', 'answer'}:
            return new_riddle
        else:
            return None
    except:
        return None

async def xo_emojinator(number: list[0, 1, 2]):
        match number:
            case 0:
                return "🟪"
            case 1:
                return "🔵"
            case 2:
                return "❌"

async def get_language(user: types.User):
    code = user.language_code
    if code in languages.langs:
        return code
    else:
        return "en"

# Чтобы не писать много кода и заменить файл keyboards.py, который раньше был у меня, я создал эту функцию. Она подходит для простеньких кнопок, остальное будет писаться в main.py
async def simple_keyboards(user=None, **buttons):
    builder = InlineKeyboardBuilder()
    for item in buttons.items():
        # Прикол в том, что ключи в словаре написаны с маленькой буквы, а кнопки с заглавной, т.е. конфликта быть не может
        if item[1] in languages.buttons[await get_language(user)].keys() and user != None:
            text = languages.buttons[await get_language(user)][item[1]]
        else:
            text = item[1]
        button = types.InlineKeyboardButton(text=text, callback_data=item[0])
        builder.add(button)
    return builder.as_markup()