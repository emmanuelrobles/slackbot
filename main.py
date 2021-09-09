import asyncio
import schedule
import os
from rx import operators as ops
from bot_init.slackbot import Slackbot
from messages.handler import message_handler


async def main():

    # init the bot
    bot = Slackbot()

    # add message handler
    observable = message_handler(bot.get_stream())

    # pipe the send message func and subscribe
    observable.pipe(
        ops.do_action(lambda res: bot.send_message(res)),
    ).subscribe(
        on_error=lambda err: print(err)
    )

    await scheduler()
    from threading import Event
    Event().wait()


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(5)

asyncio.run(main())
