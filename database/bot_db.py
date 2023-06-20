# SQL - Structured Query Language
# СУБД - Система Управления Базой Данных
# CRUD - Create Reed Update Delete
import random
import sqlite3


def sql_create():
    global db, cursor
    db = sqlite3.connect("bot.sqlite3")
    cursor = db.cursor()

    if db:
        print("База данных подключена!")

    db.execute("CREATE TABLE IF NOT EXISTS anketa "
               "(id INTEGER PRIMARY KEY AUTOINCREMENT,"
               "telegram_id INTEGER UNIQUE NOT NULL,"
               "username VARCHAR (100),"
               "name VARCHAR (100) NOT NULL,"
               "age INTEGER NOT NULL,"
               "gender VARCHAR (10),"
               "region TEXT,"
               "photo TEXT)")
    db.commit()


async def sql_command_insert(state):
    async with state.proxy() as data:
        cursor.execute(
            "INSERT INTO anketa "
            "(telegram_id, username, name, age, gender, region, photo) "
            "VALUES (?, ?, ?, ?, ?, ?, ?)",
            tuple(data.values())
        )
        db.commit()


async def sql_command_random():
    users = cursor.execute("SELECT * FROM anketa").fetchall()
    random_user = random.choice(users)
    return random_user


async def sql_command_all():
    return cursor.execute("SELECT * FROM anketa").fetchall()


async def sql_command_all_ids():
    return cursor.execute("SELECT telegram_id FROM anketa").fetchall()


async def sql_command_delete(user_id):
    cursor.execute("DELETE FROM anketa WHERE id = ?", (user_id,))
    db.commit()
