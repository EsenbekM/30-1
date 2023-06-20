from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import bot, ADMINs
from database.bot_db import sql_command_all, sql_command_delete, sql_command_all_ids


async def ban(message: types.Message):
    if message.chat.type != "private":
        if message.from_user.id not in ADMINs:
            await message.answer("Ты не мой босс!")
        elif not message.reply_to_message:
            await message.answer("Команда должна быть ответом на сообщение!")
        else:
            await message.delete()
            await bot.kick_chat_member(
                message.chat.id,
                message.reply_to_message.from_user.id
            )
            await message.answer(
                f"{message.from_user.first_name} братан, кикнул "
                f"{message.reply_to_message.from_user.full_name}"
            )
    else:
        await message.answer("Пиши в группе!")


async def delete_data(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all()
        for user in users:
            await message.answer_photo(
                user[-1],
                caption=f"{user[3]} {user[4]} "
                        f"{user[5]} {user[6]}"
                        f"\n\n{user[2]}",
                reply_markup=InlineKeyboardMarkup().add(
                    InlineKeyboardButton(f"Удалить {user[3]}",
                                         callback_data=f"delete {user[0]}")
                ))


async def complete_delete(callback: types.CallbackQuery):
    await sql_command_delete(callback.data.replace("delete ", ""))
    await callback.answer("Удалено с БД!", show_alert=True)
    await callback.message.delete()


async def rassylka(message: types.Message):
    if message.from_user.id not in ADMINs:
        await message.answer("Ты не мой босс!")
    else:
        users = await sql_command_all_ids()
        for user in users:
            await bot.send_message(user[0], message.text[3:])


def register_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(ban, commands=['ban'], commands_prefix='!/')
    dp.register_message_handler(rassylka, commands=['R'])
    dp.register_message_handler(delete_data, commands=['del'])
    dp.register_callback_query_handler(
        complete_delete,
        lambda callback: callback.data and callback.data.startswith("delete ")
    )
