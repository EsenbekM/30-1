from aiogram import types, Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, dp
from .keyboards import start_markup
from database.bot_db import sql_command_random


# @dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id,
                           f"Салалекум хозяин {message.from_user.full_name}",
                           reply_markup=start_markup)
    # await message.answer("This is an answer method")
    # await message.reply("This is a reply method")


# @dp.message_handler(commands=['quiz'])
async def quiz_1(message: types.Message) -> None:
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_1")
    markup.add(next_button)

    quiestion = "By whom invented Python?"
    answers = [
        "Harry Potter",
        "Putin",
        "Guido Van Rossum",
        "Voldemort",
        "Griffin",
        "Linus Torvalds",
    ]

    # await bot.send_poll()
    await message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать!",
        open_period=10,
        reply_markup=markup
    )


# @dp.message_handler(commands=['cat'])
async def cat_handler(message: types.Message) -> None:
    await message.answer_photo(
        photo="https://i.kym-cdn.com/entries/icons/original/000/043/403/cover3.jpg"
    )

    photo = open("media/images/cat.jpg", "rb")
    await bot.send_photo(
        chat_id=message.from_user.id,
        photo=photo
    )


async def get_random_user(message: types.Message) -> None:
    random_user = await sql_command_random()
    await message.answer_photo(random_user[-1],
                               caption=f"{random_user[3]} {random_user[4]} "
                                       f"{random_user[5]} {random_user[6]}"
                                       f"\n\n{random_user[2]}")


def register_handlers_commands(dp: Dispatcher):
    dp.register_message_handler(start_command, commands=['start'])
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_message_handler(cat_handler, Text(equals="котики", ignore_case=True))
    dp.register_message_handler(get_random_user, Text(equals="get", ignore_case=True))
