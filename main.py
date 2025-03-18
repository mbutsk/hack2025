import logging
import asyncio
import sys
from aiogram.methods.delete_webhook import DeleteWebhook
from aiogram import types, F
from aiogram.filters.command import Command
from bot import bot, dp
import ai
import os
import json

# AI
sessions = {}

banned = [1857760594]

@dp.message(Command("riddle"))
async def riddle(message: types.Message):
    if message.from_user.id in banned:
        return await message.answer("А робот может написать симфонию? Может превратить кусок мяса в шедевр исскусства?")
    else:
        think_msg = await message.answer("💬")

        while True:
            session = ai.DSSession(ai.system_prompts["riddle"])
            answer  = (await session.chat())["answer"]
            answer  = answer.replace("```json", "").replace("```", "")

            riddle = ai.riddle_dicter(answer)
            if not riddle:
                break

        formatted_answer = f"**{riddle['question']}\n\n\n{riddle['answer']}"
        await think_msg.delete()
        if len(formatted_answer) > 4096:
            os.makedirs(".temp", exist_ok=True)
            filepath = f'.temp/{message.chat.id} riddle.txt'
            with open(filepath, "w") as f:
                f.write(formatted_answer)
            await message.answer_document(types.FSInputFile(filepath))
            os.remove(filepath)
        else:
            await message.answer(formatted_answer)

@dp.message(F.start("ананастасия "))
async def chat(message: types.Message):
    if message.from_user.id in banned:
        await message.answer("А робот может написать симфонию? Может превратить кусок мяса в шедевр исскусства?")
    else:
        think_msg = await message.answer("💬")
        if message.chat.id not in sessions:
            sessions[message.chat.id] = ai.DSSession(ai.system_prompts["helper"])
        
        response = await sessions[message.chat.id].chat(message.text.replace("ананастасия ", ""))

        think = response["think"]
        answer = response["answer"]
        
        formatted_answer = f"Мысли: {think}\n\n\nОтвет: {answer}"

        await think_msg.delete()

        if len(formatted_answer) > 4096:
            os.makedirs(".temp", exist_ok=True)
            filepath = f'.temp/{message.chat.id} answer.txt'
            with open(filepath, "w") as f:
                f.write(formatted_answer)
            await message.answer_document(types.FSInputFile(filepath))
            os.remove(filepath)
        else:
            await message.answer(formatted_answer)

@dp.message(Command('clear'))
async def clear_ai(message: types.Message):
    if message.from_user.id in banned:
        return await message.answer("А робот может написать симфонию? Может превратить кусок мяса в шедевр исскусства?")
    else:
        global sessions
        del sessions[message.chat.id]
        await message.answer("Session cleared.")

async def main() -> None:
    # And the run events dispatching
    await bot(DeleteWebhook(drop_pending_updates=True))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
