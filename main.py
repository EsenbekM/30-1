from aiogram import Bot, Dispatcher, types, executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from decouple import config
import logging

TOKEN = config("TOKEN")
bot = Bot(TOKEN)
dp = Dispatcher(bot=bot)


@dp.message_handler(commands=['start'])
async def start_command(message: types.Message) -> None:
    await bot.send_message(message.chat.id, f"Салалекум хозяин {message.from_user.full_name}")
    await message.answer("This is an answer method")
    await message.reply("This is a reply method")


@dp.message_handler(commands=['quiz'])
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


@dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    quiestion = "Что такое Кефтеме?"
    answers = [
        "Тяги",
        "Это радость",
        "Ноут",
        "Мем",
        "Обувь",
    ]

    # await bot.send_poll()
    await callback.message.answer_poll(
        question=quiestion,
        options=answers,
        is_anonymous=False,
        type='quiz',
        correct_option_id=2,
        explanation="Стыдно не знать!",
        open_period=10,
    )


@dp.message_handler(content_types=['text'])
async def echo(message: types.Message) -> None:
    await bot.send_message(message.chat.id, message.text)


@dp.message_handler(content_types=['sticker'])
async def echo(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
