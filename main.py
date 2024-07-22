import logging
import asyncio
import json
from random import randint
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command

logging.basicConfig(level=logging.INFO, filename="py_log.log")

bot = Bot(token=PASSWORLD, parse_mode="HTML")

dp = Dispatcher()

@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("Здравствуй, " + message.from_user.first_name + "!")
    await message.answer(
        "Нажми:\n"
        "/start - как будто ты тут в первый раз\n"
        "/classic_poem - случаное классическое стихотворение\n"
        "/modern_poem - случайное современное стихотворение\n"
    )

@dp.message(Command("classic_poem"))
async def classic_poem(message: types.Message):
    file_path = "classic_poems/" + str(randint(1, 10)) + ".txt"
    with open(file_path) as file:
        await message.answer(file.read())

@dp.message(Command("modern_poem"))
async def modern_poem(message: types.Message):
    file_path = "modern_poems/" + str(randint(1, 10)) + ".txt"
    with open(file_path) as file:
        await message.answer(file.read())

@dp.message()
async def help(message: types.Message):
    await message.answer("Такой команды нет!(\nВыбери команду из меню:")
    await message.answer(
        "/start - как будто ты тут в первый раз\n"
        "/classic_poem - случаное классическое стихотворение\n"
        "/modern_poem - случайное современное стихотворение\n"
    )


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())