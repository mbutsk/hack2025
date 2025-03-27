import logging
import asyncio
import sys
from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram import types, F
from aiogram.filters import Command
from bot import *
import utils
import db
from dictionaries import replicas, persons, stickers, artist
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
import random
import ai
import db
import time

# В аиограме со State можно работать только когда они в группах
class EnterYearGroup(StatesGroup):
    EnterYear = State()


class RiddleGroup(StatesGroup):
    Riddle = State()


class ArtistGroup(StatesGroup):
    Artist = State()


class AIGroup(StatesGroup):
    AI = State()

# Инициализация датабазы
database = db.Database()
database.create("users", language="TEXT DEFAULT NULL",
                id="INTEGER UNIQUE", time="INTEGER")

# Команды всякие. Комментировать буду только интересное
@router.message(Command('start'))
async def start(message: types.Message):
    await message.answer(replicas[await utils.get_language(message.from_user)]["hi"], reply_markup=await utils.simple_keyboards(message.from_user, start="start"))


@router.callback_query(F.data == "start")
async def start_game(callback: types.CallbackQuery):
    # Добавление юзера в датабазу, если его там еще нет
    try:
        database.insert("users", id=callback.from_user.id, time=time.time())
    except:
        pass

    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker(stickers["pigeon"])
    await message.answer(replicas[language]["pigeon"], reply_markup=await utils.simple_keyboards(callback.from_user, read_pigeon="read"))

# Смена языка
@router.message(Command('change'))
async def change(message: types.Message):
    try:
        language = await utils.get_language(message.from_user)
        match language:
            case "ru":
                new = "en"
            case "en":
                new = "ru"
        database.update("users", "language", new,
                        f"id = {message.from_user.id}")
    except:
        pass


@router.callback_query(F.data == "read_pigeon")
async def read_pigeon(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker(stickers["envelope"])
    await message.answer(replicas[language]["johnes1"], reply_markup=await utils.simple_keyboards(callback.from_user, go_saloon="go"))


@router.callback_query(F.data == "go_saloon")
async def go_saloon(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker(stickers["waiter"])
    await message.answer(f"{persons[language]["waiter"]}: {replicas[language]["waiter"]}", reply_markup=await utils.simple_keyboards(callback.from_user, agree_saloon="agree", disagree_saloon="disagree"))

# Перестрелка
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
    await asyncio.sleep(1)
    await message.answer(replicas[language]["saloon_bandits"])
    await asyncio.sleep(1)
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
        await asyncio.sleep(0.6)
        await react.delete()
    else:
        await state.clear()
        await message.answer(f"{persons[language]["you"]}: {replicas[language]["you_shoot"]}")
        await asyncio.sleep(1)
        await message.answer(f"{persons[language]["watch"]}: {replicas[language]["enter_year"]}")
        await state.set_state(EnterYearGroup.EnterYear)


@router.message(EnterYearGroup.EnterYear)
async def enter_year(message: types.Message, state: FSMContext):
    language = await utils.get_language(message.from_user)

    if message.text == "2427":
        await message.answer(f"{persons[language]["watch"]}: {replicas[language]["hq_far_away"]}")
    elif message.text == "1845":
        await state.clear()
        await message.answer_sticker(stickers["johnes"])
        await message.answer(f"{persons[language]["johnes"]}: {replicas[language]["johnes2"]}", reply_markup=await utils.simple_keyboards(message.from_user, go_future="go"))
    else:
        await message.answer(f"{persons[language]["watch"]}: {replicas[language]["hq_not_found"]}")


@router.callback_query(F.data == "go_future")
async def go_future(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker(stickers["robot"])
    await message.answer(replicas[language]["robot1"])
    await asyncio.sleep(1)
    await message.answer(replicas[language]["robot2"])
    await asyncio.sleep(2)
    await message.answer(replicas[language]["you_mind"])
    await asyncio.sleep(2)
    await message.answer(replicas[language]["guard1"], reply_markup=await utils.simple_keyboards(callback.from_user, go_guard="go2"))


@router.callback_query(F.data == "go_guard")
async def go_guard(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(f"{persons[language]["guard"]}: {replicas[language]["guard2"]}")
    await asyncio.sleep(2)
    await message.answer(f"{persons[language]["you"]}: {replicas[language]["guard3"]}")
    await asyncio.sleep(2)
    await message.answer(f"{persons[language]["guard"]}: {replicas[language]["guard4"]}")
    await asyncio.sleep(2)
    await message.answer(replicas[language]["guard5"])
    await asyncio.sleep(2)
    await message.answer_sticker(stickers["guard"])
    await message.answer(f"{persons[language]["guard"]}: {replicas[language]["guard6"]}")
    await asyncio.sleep(1)
    await message.answer(replicas[language]["manual2"], reply_markup=await utils.simple_keyboards(callback.from_user, riddle_agree="agree", riddle_disagree="disagree"))

# Загадки!!!
@router.callback_query(F.data == "riddle_agree")
async def riddle(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    think_msg = await message.answer("💬")
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])

    while True:
        session = ai.DSSession(ai.system_prompts["riddle"])
        answer = (await session.chat())["answer"]

        riddle = await utils.riddle_dicter(answer)
        if riddle:
            break

    await state.set_state(RiddleGroup.Riddle)
    await state.set_data({
        "answer":   riddle["answer"]
    })
    print(f"это вам для теста: {riddle["answer"]}")

    await think_msg.delete()
    if len(riddle["question"]) > 4096:
        os.makedirs(".temp", exist_ok=True)
        filepath = f'.temp/{message.chat.id} riddle.txt'
        with open(filepath, "w") as f:
            f.write(riddle["question"])
        await message.answer_document(types.FSInputFile(filepath))
        os.remove(filepath)
    else:
        await message.answer(riddle["question"])


@router.message(RiddleGroup.Riddle)
async def riddle_answer(message: types.Message, state: FSMContext):
    answer = (await state.get_data())["answer"]
    await state.clear()
    language = await utils.get_language(message.from_user)
    await message.answer(replicas[language]["manual3"])
    await asyncio.sleep(1)
    if message.text == answer:
        await message.answer(replicas[language]["guard8"].format(message.from_user.first_name))
    else:
        await message.answer(replicas[language]["guard7"].format(answer))
    await asyncio.sleep(2)
    await message.answer(f"{persons[language]["watch"]}: {replicas[language]["notification"]}", reply_markup=await utils.simple_keyboards(message.from_user, read_coord="read"))


@router.callback_query(F.data == "riddle_disagree")
async def riddle_disagree(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(f"{persons[language]["watch"]}: {replicas[language]["notification"]}", reply_markup=await utils.simple_keyboards(callback.from_user, read_coord="read"))


@router.callback_query(F.data == "read_coord")
async def read_coord(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(f"{persons[language]["watch"]}: {replicas[language]["coord"].format(random.randint(1, 100), random.randint(1, 100))}", reply_markup=await utils.simple_keyboards(callback.from_user, go_coord="go"))


@router.callback_query(F.data == "go_coord")
async def go_coord(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(replicas[language]["robot_met"])
    await asyncio.sleep(1)
    await message.answer_sticker(stickers["artist"])
    await message.answer(f"{persons[language]["artist"]}: {replicas[language]["artist1"]}")
    await asyncio.sleep(1)
    await message.answer_sticker(stickers["artist"])
    await message.answer(f"{persons[language]["artist"]}: {replicas[language]["artist2"]}")
    await asyncio.sleep(2)
    await message.answer(replicas[language]["manual4"], reply_markup=await utils.simple_keyboards(callback.from_user, paint_celeb="celebrity", paint_funcode="FunCode"))

# Самая интересная мини игра с художником
@router.callback_query(F.data.startswith("paint"))
async def paint(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    theme = callback.data.replace("paint_", "")
    person = random.choice(list(artist[language][theme].items()))
    await state.set_state(ArtistGroup.Artist)
    await state.set_data({
        "current": person,
        "tryed":     []
    })
    await message.answer_photo(person[0])


@router.message(ArtistGroup.Artist)
async def paint_guess(message: types.Message, state: FSMContext):
    language = await utils.get_language(message.from_user)
    this_persons = (await state.get_data())["current"][1]
    persons_guess = [s.strip().lower() for s in message.text.split("+")]
    if isinstance(persons_guess, list) and len(persons_guess) == 2:
        if sorted(this_persons) == sorted(persons_guess):
            await state.clear()
            await message.answer_sticker(stickers["artist"])
            await message.answer(f"{persons[language]["artist"]}: {replicas[language]["artist3"]}", reply_markup=await utils.simple_keyboards(message.from_user, go_racing="go3"))
        else:
            await message.answer_sticker(stickers["artist"])
            await message.answer(f"{persons[language]["artist"]}: {replicas[language]["wrong_art"]}", reply_markup=await utils.simple_keyboards(message.from_user, change_art="change"))
    else:
        await message.answer(replicas[language]["manual5"])


@router.callback_query(F.data == "change_art")
async def change_art(callback: types.CallbackQuery, state: FSMContext):
    language = await utils.get_language(callback.from_user)
    current = (await state.get_data())["current"][0]
    tryed: list = (await state.get_data())["tryed"]
    tryed.append(current)
    all_persons = artist[language]["celeb"] | artist[language]["funcode"]
    available = {key: value for key, value in all_persons.items()
                 if key not in tryed}
    if available == {}:
        available = all_persons
    person = random.choice(list(available.items()))
    await state.update_data({
        "tryed": tryed,
        "current": person,
    })
    await callback.message.answer_photo(person[0])

# Скачки
@router.callback_query(F.data == "go_racing")
async def go_racing(callback: types.CallbackQuery, state: FSMContext):
    await state.clear()
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(replicas[language]["robot_met"])
    await asyncio.sleep(1)
    await message.answer_sticker(stickers["stableman"])
    await message.answer(f"{persons[language]["stableman"]}: {replicas[language]["stableman1"]}", reply_markup=await utils.simple_keyboards(bet1="1🐴", bet2="2🐴", bet3="3🐴"))


@router.callback_query(F.data.startswith("bet"))
async def racing(callback: types.CallbackQuery):
    message = callback.message
    racing = utils.Racing()
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    bet = callback.data.replace("bet", "")
    while not racing.is_finished:
        # Если изменять сообщение, можно попасться на рейт-лимит телеграма
        msg = await message.answer(str(racing))
        await asyncio.sleep(1)
        await racing.go()
        await msg.delete()
    msg = await message.answer(str(racing))
    if racing.winner != bet:
        await message.answer_sticker(stickers["stableman"])
        await message.answer(f"{persons[language]["stableman"]}: {replicas[language]["stableman2"]}", reply_markup=await utils.simple_keyboards(bet1="1🐴", bet2="2🐴", bet3="3🐴"))
    else:
        await message.answer_sticker(stickers["stableman"])
        await message.answer(f"{persons[language]["stableman"]}: {replicas[language]["stableman3"]}",  reply_markup=await utils.simple_keyboards(callback.from_user, go_yennefer="go3"))

# Перестрелка 2
@router.callback_query(F.data == "go_yennefer")
async def yennefer_shooting(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(replicas[language]["nefer_guards"], reply_markup=await utils.simple_keyboards(callback.from_user, call_g="call_g"))
    await state.set_data({
        "killed": 0
    })


@router.callback_query(F.data == "call_g")
async def call_g(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await asyncio.sleep(random.randint(2, 10))
    react = await message.answer(replicas[language]["shoot"], reply_markup=await utils.simple_keyboards(callback.from_user, shoot_g="shoot"))
    await asyncio.sleep(0.6)
    await react.delete()


@router.callback_query(F.data == "shoot_g")
async def shoot_g(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    data = await state.get_data()
    killed = data["killed"]

    await state.update_data({
        "killed": killed + 1
    })
    if killed != 2:
        await asyncio.sleep(random.randint(2, 10))
        react = await message.answer(replicas[language]["shoot"], reply_markup=await utils.simple_keyboards(callback.from_user, shoot_g="shoot"))
        await asyncio.sleep(0.6)
        await react.delete()
    else:
        await state.clear()
        await message.answer(f"{persons[language]["you"]}: {replicas[language]["you_shoot"]}")
        await asyncio.sleep(1)
        await message.answer_sticker(stickers["nefer"])
        await message.answer(f"*NASTASYA*: {replicas[language]["nefer1"]}", reply_markup=await utils.simple_keyboards(callback.from_user, ga_nefer_ag="agree", ga_nefer_dis="disagree"))


@router.callback_query(F.data.startswith("ga_nefer"))
async def nefer_game(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer_sticker(stickers["nefer"])
    if callback.data == "ga_nefer_dis":
        await message.answer(f"*NASTASYA*: {replicas[language]["nefer2"]}")
    else:
        await message.answer(f"*NASTASYA*: {replicas[language]["nefer3"]}")
    await asyncio.sleep(1)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer4"]}")
    await asyncio.sleep(3)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer5"]}")
    await asyncio.sleep(1)
    session = utils.TicTacToe()
    await state.set_data({
        "session": session
    })
    await message.answer("XO", reply_markup=await session.as_markup())


# Крестики нолики. По расчетам, победа человека невозможна, но на всякий случай я сделаю для нее хендл
@router.callback_query(F.data.startswith("xo "))
async def handle_xo_callback(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])

    place = callback.data.replace("xo ", "").split("-")
    data = (await state.get_data())
    if data != {}:
        session: utils.TicTacToe = data["session"]
        if session.board[int(place[0])][int(place[1])] == 0:
            await session.place(int(place[0]), int(place[1]), 2)
            if await session.check_win():
                await message.edit_reply_markup(reply_markup=await session.as_markup())
                await state.clear()
                await message.answer_sticker(stickers["nefer"])
                await message.reply(f"*NASTASYA*: {replicas[language]["nefer7"]}")
                await rps(callback)
                return
            elif await session.check_tie():
                await state.clear()
                await message.answer_sticker(stickers["nefer"])
                await message.reply(f"*NASTASYA*: {replicas[language]["nefer8"]}")
                await rps(callback)
                await message.edit_reply_markup(reply_markup=await session.as_markup())
                return
            else:
                await session.ai_place()
                if await session.check_win():
                    await state.clear()
                    await message.answer_sticker(stickers["nefer"])
                    await message.reply(f"*NASTASYA*: {replicas[language]["nefer10"]}")
                    await message.edit_reply_markup(reply_markup=await session.as_markup())
                    await rps(callback)
                elif await session.check_tie():
                    await state.clear()
                    await message.answer_sticker(stickers["nefer"])
                    await message.reply(f"*NASTASYA*: {replicas[language]["nefer8"]}")
                    await rps(callback)
                    await message.edit_reply_markup(reply_markup=await session.as_markup())
                    return
                else:
                    await message.edit_reply_markup(reply_markup=await session.as_markup())
        else:
            await message.answer_sticker(stickers["nefer"])
            await message.reply(f"*NASTASYA*: {replicas[language]["nefer6"]}")
    else:
        await message.answer_sticker(stickers["nefer"])
        await message.answer(f"*NASTASYA*: {replicas[language]["nefer9"]}")

# Камень ножниув бумага
async def rps(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])

    await asyncio.sleep(1)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer11"]}", reply_markup=await utils.simple_keyboards(message.from_user, rps_r="👊🏻", rps_p="✋🏻", rps_s="✌🏻"))


@router.callback_query(F.data.startswith("rps_"))
async def end(callback: types.CallbackQuery):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await message.answer(replicas[language]["nefer12"])
    g = callback.data.replace("rps_", "")
    ai_g = {
        "r": "📃",
        "p": "✂️",
        "s": "🪨"
    }[g]
    await asyncio.sleep(1)
    await message.answer(ai_g)
    await asyncio.sleep(2)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer13"]}")
    await asyncio.sleep(3)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer14"]}")
    await asyncio.sleep(8)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer15"]}")
    await asyncio.sleep(8)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer16"]}")
    await asyncio.sleep(4)
    await message.answer_sticker(stickers["nefer"])
    await message.answer(f"*NASTASYA*: {replicas[language]["nefer17"]}")
    await asyncio.sleep(5)
    old_time = database.select(
        ["time"], "users", f"id={callback.from_user.id}")[0][0]
    await message.answer(replicas[language]["end"].format(utils.format_time(time.time() - old_time)), reply_markup=await utils.simple_keyboards(callback.from_user, pr_helper="helper", pr_NASTASYA="NASTASYA"))

# Смена промпта
@router.callback_query(F.data.startswith("pr_"))
async def set_prompt(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await state.clear()
    await state.set_state(AIGroup.AI)
    await state.set_data({
        "session":  ai.DSSession(ai.system_prompts[callback.data.replace("pr_", "")])
    })
    await message.answer(replicas[language]["changed"])

# ИИ
@router.message(AIGroup.AI)
async def chat(message: types.Message, state: FSMContext):
    think_msg = await message.answer("💬")
    session: ai.DSSession = (await state.get_data())["session"]
    response = await session.chat(message.text)

    think = response["think"]
    answer = response["answer"]

    formatted_answer = f"*Мысли*: {think}\n\n\n*Ответ*: {answer}"

    await think_msg.delete()
    markup = await utils.simple_keyboards(message.from_user, clear_s="clear", pr_helper="helper", pr_NASTASYA="NASTASYA")
    if len(formatted_answer) > 4096:
        os.makedirs(".temp", exist_ok=True)
        filepath = f'.temp/{message.chat.id} answer.txt'
        with open(filepath, "w") as f:
            f.write(formatted_answer)
        await message.answer_document(types.FSInputFile(filepath), reply_markup=markup)
        os.remove(filepath)
    else:
        await message.answer(formatted_answer, reply_markup=markup)

# Очистка сессии
@router.callback_query(F.data == "clear_s")
async def clear_ai(callback: types.CallbackQuery, state: FSMContext):
    message = callback.message
    language = await utils.get_language(callback.from_user)
    await callback.answer(replicas[language]["inline"])
    await state.clear()
    await message.answer(replicas[language]["choosepr"], reply_markup=await utils.simple_keyboards(message.from_user, pr_helper="helper", pr_NASTASYA="NASTASYA"))


# Запуск бота
async def main() -> None:
    await bot(DeleteWebhook(drop_pending_updates=True))
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
