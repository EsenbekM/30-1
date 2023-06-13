from aiogram import types, Dispatcher
from config import bot


# @dp.message_handler(content_types=['text'])
async def echo_text(message: types.Message) -> None:
    bad_words = ['дурак', 'html', 'js']
    for word in bad_words:
        if word in message.text.lower().replace(" ", ""):
            # await bot.delete_message(message.chat.id, message.message_id)
            await message.delete()
            await message.answer(
                f"Не матерись @{message.from_user.username}\n"
                f"сам ты {word}"
            )

    if message.text.startswith('.'):
        # await bot.pin_chat_message(message.chat.id, message.message_id)
        await message.pin()

    if message.text == "dice":  # 🎲🎯🎰🎳🏀⚽️
        # await bot.send_dice()
        a = await message.answer_dice()
        # print(a.dice.value)
    # print(await message.chat.get_administrators())


# @dp.message_handler(content_types=['sticker'])
async def echo_sticker(message: types.Message) -> None:
    await bot.send_sticker(message.chat.id, message.sticker.file_id)


def register_handlers_extra(dp: Dispatcher):
    dp.register_message_handler(echo_text, content_types=['text'])
    dp.register_message_handler(echo_sticker, content_types=['sticker'])
