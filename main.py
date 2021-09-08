import asyncio
from collections import namedtuple

import rx.subject
import schedule
import re
import random
import os

from rx import Observable
from rx import operators as ops
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.web import WebClient
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest
from pathlib import Path
from dotenv import load_dotenv

from consts import lines
import incoming_messages

from routine_messages import goodMorningMessage, preeStandupMessage, noonMessage, goodNightMessage

# load env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

# client setup
client = SocketModeClient(
    app_token=os.environ['APP_TOKEN'],
    web_client=WebClient(os.environ['WEB_CLIENT_TOKEN'])
)

channel = os.environ['CHANNEL']

messageSubject = rx.subject.Subject()


async def main():

    setup_processing()

    client.socket_mode_request_listeners.append(process)
    client.connect()
    weekday_job(goodMorningMessage, '07:00')
    weekday_job(preeStandupMessage, '10:30')
    weekday_job(noonMessage, '12:00')
    weekday_job(goodNightMessage, '17:00')

    await scheduler()
    from threading import Event
    Event().wait()


def weekday_job(x, t=None):
    from datetime import datetime
    week = datetime.today().weekday()
    if t is not None and week < 5:
        schedule.every().day.at(t).do(x, client, channel)


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(5)


# Message processing
def process_message(event: dict, client: SocketModeClient):
    incoming_messages.pierre_messages(event, client)
    incoming_messages.eye_reaction_message(event, client)
    incoming_messages.costco_lines(event, client)
    incoming_messages.shhh_line(event, client)
    incoming_messages.cache_emoji(event, client)
    incoming_messages.beach_emoji(event, client)
    incoming_messages.pic_mad_reaction(event, client)
    incoming_messages.pic_bug(event, client)


# Process events
def process(client: SocketModeClient, req: SocketModeRequest):
    Message = namedtuple('Message', ['client', 'request'])
    messageSubject.on_next(Message(client, req))

    # if req.type == "events_api":
    #     # Acknowledge the request anyway

    #
    #     # Add a reaction to the message if it's a new message
    #     if req.payload["event"]["type"] == "message" \
    #             and req.payload["event"].get("subtype") is None:
    #         process_message(req.payload["event"], client)


def setup_processing():
    def acknowledge_message(msg):
        response = SocketModeResponse(envelope_id=msg.request.envelope_id)
        client.send_socket_mode_response(response)

    messageSubject.pipe(
        ops.filter(lambda msg:
                   msg.request.type == 'events_api'),
        ops.do_action(lambda msg:acknowledge_message(msg)),

    ).subscribe()


asyncio.run(main())
