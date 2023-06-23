import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from config import ADMINs, bot
from database.bot_db import sql_command_all_ids
from apscheduler.triggers.cron import CronTrigger
from apscheduler.triggers.interval import IntervalTrigger
from apscheduler.triggers.date import DateTrigger


async def go_to_sleep(text):
    users = await sql_command_all_ids()
    for user in users:
        await bot.send_message(
            user[0], f"ИДи спаать {text} !"
        )


async def wake_up():
    video = open("media/video/video.mp4", "rb")
    for user in ADMINs:
        await bot.send_video(
            chat_id=user,
            video=video,
            caption=f"Вставааааай!!!"
        )


async def set_scheduler():
    scheduler = AsyncIOScheduler(timezone="Asia/Bishkek")
    # scheduler.add_job(
    #     go_to_sleep,
    #     CronTrigger(
    #         hour=20,
    #         minute=31,
    #         start_date=datetime.datetime.now()
    #     ),
    #     kwargs={"text": "balapan"}
    # )
    scheduler.add_job(
        wake_up,
        IntervalTrigger(
            seconds=20,
            start_date=datetime.datetime.now()
        ),
    )
    # scheduler.add_job(
    #     go_to_sleep,
    #     DateTrigger(
    #         run_date=datetime.datetime(year=2023, month=12, day=12)
    #     ),
    #     kwargs={"text": "balapan"}
    # )

    scheduler.start()
