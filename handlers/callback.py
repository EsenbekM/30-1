from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# @dp.callback_query_handler(text="next_button_1")
async def quiz_2(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup()
    next_button = InlineKeyboardButton("NEXT", callback_data="next_button_2")
    markup.add(next_button)

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
        reply_markup=markup
    )


async def quiz_3(callback: types.CallbackQuery):
    await callback.message.answer("Это все!")


def register_handlers_callback(dp: Dispatcher):
    dp.register_callback_query_handler(quiz_2, text="next_button_1")
    dp.register_callback_query_handler(quiz_3, text="next_button_2")
