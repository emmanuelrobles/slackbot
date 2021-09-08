import asyncio
from collections import namedtuple
import rx.subject
import schedule
import re
import random
import os
from rx import Observable
from rx import operators as ops
from pathlib import Path
from dotenv import load_dotenv

from bot_init.slackbot import slack_bot_init
from consts import lines
import incoming_messages
from routine_messages import goodMorningMessage, preeStandupMessage, noonMessage, goodNightMessage
from models.requestmessage import RequestMessage

import bot_init


async def main():

    observable = slack_bot_init()

    observable.pipe(
        ops.do_action(lambda msg: print(msg.get_text()))
    ).subscribe()



    # weekday_job(goodMorningMessage, '07:00')
    # weekday_job(preeStandupMessage, '10:30')
    # weekday_job(noonMessage, '12:00')
    # weekday_job(goodNightMessage, '17:00')

    await scheduler()
    from threading import Event
    Event().wait()


def weekday_job(x, t=None):
    from datetime import datetime
    channel = os.environ['CHANNEL']
    week = datetime.today().weekday()
    if t is not None and week < 5:
        schedule.every().day.at(t).do(x,channel)


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(5)


# # Message processing
# def process_message(event: dict, client: SocketModeClient):
#     incoming_messages.pierre_messages(event, client)
#     incoming_messages.eye_reaction_message(event, client)
#     incoming_messages.costco_lines(event, client)
#     incoming_messages.shhh_line(event, client)
#     incoming_messages.cache_emoji(event, client)
#     incoming_messages.beach_emoji(event, client)
#     incoming_messages.pic_mad_reaction(event, client)
#     incoming_messages.pic_bug(event, client)



asyncio.run(main())
