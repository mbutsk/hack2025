import logging
import asyncio
import sys
from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram import types, F
from aiogram.filters import Command
from bot import *
import utils
import db
from languages import replicas, persons
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random

class EnterYearGroup(StatesGroup):
    EnterYear = State()

database = db.Database()

ai_sessions = {}

xo_sessions = {}

@router.message(Command('start'))
async def start(message: types.Message, state: FSMContext):
    await message.answer(replicas[await utils.get_language(message.from_user)]["hi"], reply_markup=await utils.simple_keyboards(message.from_user, start="start"))

@router.callback_query(F.data == "start")
async def start_game(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker("CAACAgIAAxkBAAEOJBhn39vQjvLL9ULGHLLPwz0YtLlhcQACoG4AAvmhAUst5M-iMSKMyDYE")
    await message.answer(replicas[language]["pigeon"], reply_markup=await utils.simple_keyboards(callback.from_user, read_pigeon="read"))

@router.callback_query(F.data == "read_pigeon")
async def read_pigeon(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker("CAACAgIAAxkBAAEOJTRn4Vvo8zejEbZBOBYFkLrLGgk_UwACsmoAAp23EUvj9WFZmc85YDYE")
    await message.answer(replicas[language]["johnes1"], reply_markup=await utils.simple_keyboards(callback.from_user, go_saloon="go"))

@router.callback_query(F.data == "go_saloon")
async def go_saloon(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker("CAACAgIAAxkBAAEOJURn4WCNhjqlsBnK1bJiqNmQhQqcnAACFmcAAguhCUvCaKv9ReYFdDYE")
    await message.answer(f"{persons[language]["waiter"]}: {replicas[language]["waiter"]}", reply_markup=await utils.simple_keyboards(callback.from_user, agree_saloon="agree", disagree_saloon="disagree"))

@router.callback_query(F.data.in_(["agree_saloon", "disagree_saloon"]))
async def saloon(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    if callback.data == "agree_saloon":
        time = 0.7
    else:
        time = 1
    
    await state.set_data({
        "time":    time,
        "killed":  0
    })

    await message.answer(f"{persons[language]["you"]}: {replicas[language]["saloon_you"]}")
    await asyncio.sleep(0.5)
    await message.answer(replicas[language]["saloon_bandits"])
    await asyncio.sleep(0.5)
    await message.answer(replicas[language]["manual1"], reply_markup=await utils.simple_keyboards(callback.from_user, call="call"))

@router.callback_query(F.data == "call")
async def call(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    data = await state.get_data()
    
    await asyncio.sleep(random.randint(2, 10))
    react = await message.answer(replicas[language]["shoot"], reply_markup=await utils.simple_keyboards(callback.from_user, shoot="shoot"))
    await asyncio.sleep(data["time"])
    await react.delete()

@router.callback_query(F.data == "shoot")
async def shoot(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    data = await state.get_data()
    killed = data["killed"]

    await state.update_data({
        "killed": killed + 1
    })
    if killed != 4:
        await asyncio.sleep(random.randint(2, 10))
        react = await message.answer(replicas[language]["shoot"], reply_markup=await utils.simple_keyboards(callback.from_user, shoot="shoot"))
        await asyncio.sleep(data["time"])
        await react.delete()
    else:
        await message.answer(f"{persons[language]["you"]}: {replicas[language]["you_shoot"]}")
        await asyncio.sleep(1)
        await message.answer(f"{persons[language]["watch"]}: {replicas[language]["enter_year"]}")
        await state.set_state(EnterYearGroup.EnterYear)

@router.message(EnterYearGroup.EnterYear)
async def enter_year(message: types.Message, state: FSMContext):
    await state.clear()

    


@test_router.message(Command("racing"))
async def racing(message: types.Message):
    racing = utils.Racing()
    while not racing.is_finished:
        msg = await message.answer(str(racing))
        await asyncio.sleep(1)
        await racing.go()
        await msg.delete()
    msg = await message.answer(str(racing))
    await msg.edit_text(str(racing) + "\n" + f"Победила лошадь номер {racing.winner}")

@test_router.message(Command("xo"))
async def xo(message: types.Message):
    xo_session = utils.TicTacToe()
    xo_sessions[message.chat.id] = xo_session
    await message.answer("XO", reply_markup=await xo_session.as_markup())

@test_router.callback_query(lambda callback: callback.data.startswith("xo "))
async def handle_xo_callback(callback: types.CallbackQuery):
    message = callback.message
    await callback.answer("оп")
    if message.chat.id in xo_sessions:
        place = callback.data.replace("xo ", "").split("-")
        
        xo_session: utils.TicTacToe = xo_sessions[message.chat.id]
        if xo_session.board[int(place[0])][int(place[1])] == 0:
            await xo_session.place(int(place[0]), int(place[1]), 2)
            if await xo_session.check_win():
                await message.edit_reply_markup(reply_markup=await xo_session.as_markup())
                await message.reply(f"Победил игрок!")
                del xo_sessions[message.chat.id]
                return
            elif await xo_session.check_tie():
                await message.reply("ничья уф")
                del xo_sessions[message.chat.id]
                await message.edit_reply_markup(reply_markup=await xo_session.as_markup())
                return
            else:
                await xo_session.ai_place()
                if await xo_session.check_win():
                    await message.reply(f"Победил ИИ!")
                    del xo_sessions[message.chat.id]
                elif await xo_session.check_tie():
                    await message.reply("ничья уф")
                    del xo_sessions[message.chat.id]
                    await message.edit_reply_markup(reply_markup=await xo_session.as_markup())
                    return
            await message.edit_reply_markup(reply_markup=await xo_session.as_markup())
        else:
            await message.reply("нет. я сказал нет!!")
    else:
        await message.reply("поздно брат")


# @test_router.message(Command("riddle"))
# async def riddle(message: types.Message):
#     think_msg = await message.answer("💬")

#     while True:
#         session = ai.DSSession(ai.system_prompts["riddle"])
#         answer  = (await session.chat())["answer"]

#         riddle = await utils.riddle_dicter(answer)
#         if riddle:
#             break

#     formatted_answer = f"**{riddle['question']}\n\n\n{riddle['answer']}"
#     await think_msg.delete()
#     if len(formatted_answer) > 4096:
#         os.makedirs(".temp", exist_ok=True)
#         filepath = f'.temp/{message.chat.id} riddle.txt'
#         with open(filepath, "w") as f:
#             f.write(formatted_answer)
#         await message.answer_document(types.FSInputFile(filepath))
#         os.remove(filepath)
#     else:
#         await message.answer(formatted_answer)

# @test_router.message(F.start("ананастасия "))
# async def chat(message: types.Message):
#     think_msg = await message.answer("💬")
#     if message.chat.id not in ai_sessions:
#         ai_sessions[message.chat.id] = ai.DSSession(ai.system_prompts["helper"])
    
#     response = await ai_sessions[message.chat.id].chat(message.text.replace("ананастасия ", ""))

#     think = response["think"]
#     answer = response["answer"]
    
#     formatted_answer = f"Мысли: {think}\n\n\nОтвет: {answer}"

#     await think_msg.delete()

#     if len(formatted_answer) > 4096:
#         os.makedirs(".temp", exist_ok=True)
#         filepath = f'.temp/{message.chat.id} answer.txt'
#         with open(filepath, "w") as f:
#             f.write(formatted_answer)
#         await message.answer_document(types.FSInputFile(filepath))
#         os.remove(filepath)
#     else:
#         await message.answer(formatted_answer)

# @test_router.message(Command('clear'))
# async def clear_ai(message: types.Message):
#     global ai_sessions
#     del ai_sessions[message.chat.id]
#     await message.answer("Session cleared.")

async def main() -> None:
    # And the run events dispatching
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
