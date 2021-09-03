import asyncio
import schedule
import re
import random
import os
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.web import WebClient
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest
from pathlib import Path
from dotenv import load_dotenv

# client setup
import helpers

# load env
env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

client = SocketModeClient(
    app_token=os.environ['APP_TOKEN'],
    web_client=WebClient(os.environ['WEB_CLIENT_TOKEN'])
)

channel = os.environ['CHANNEL']

async def main():
    client.socket_mode_request_listeners.append(process)
    client.connect()
    weekday_job(goodMorningMessage, '07:00')
    await scheduler()
    from threading import Event
    Event().wait()


def weekday_job(x, t=None):
    from datetime import datetime
    week = datetime.today().weekday()
    if t is not None and week < 5:
        schedule.every().day.at(t).do(x)


async def scheduler():
    while True:
        schedule.run_pending()
        await asyncio.sleep(3)


def goodMorningMessage():
    client.web_client.chat_postMessage(
        channel=channel,
        text='Good morning peeps'
    )


def goodNightMessage():
    client.web_client.chat_postMessage(
        channel=channel,
        text='Good night!'
    )


# Message processing
def processMessage(event: dict, client: SocketModeClient):
    # if the message is from Pierre's user
    isFromPierre = event['user'] == 'U02DYBFSED6'

    if isFromPierre and helpers.chance(1, lambda: client.web_client.chat_postMessage(
            channel=channel,
            text=random.choice(helpers.bot_lines_pierre))):
        return
    if "pierre" in event['text'].lower():
        client.web_client.reactions_add(
            name="eyes",
            channel=event["channel"],
            timestamp=event["ts"]
        )
        return
    if re.match('costco|jason', event['text'].lower()):
        client.web_client.chat_postMessage(
            channel=channel,
            text=random.choice(helpers.bot_lines)
        )
        return
    if re.match(r'\bshhh*\b', event['text'].lower()):
        client.web_client.chat_postMessage(
            channel=channel,
            text=random.choice(helpers.bot_lines_shh),
            attachments=[
                {
                    "fallback": ":)",
                    "image_url": "https://media4.giphy.com/media/EKDIMDsRX3ihy/giphy.gif?cid=ecf05e47qjya842xz1a1lgv6kuk7h039bb0ak9qijue227gi&rid=giphy.gif&ct=g"
                }
            ]
        )
        return
    if re.match(r'^(?=.*\b(cache|add|put)\b)(?=.*\b(frontend|front end|fe)\b).*$', event['text'].lower()):
        client.web_client.chat_postMessage(
            channel=channel,
            text='yea, lets put it there',
            attachments=[
                {
                    "fallback": ":)",
                    "image_url": "https://media0.giphy.com/media/8wb5IPi03CM1gzjWm6/giphy.gif?cid=790b76110caa0045ebd55d910d5ffc79502c741300864090&rid=giphy.gif&ct=g "
                }
            ]
        )
        return
    if re.match(r'^(?=.*\b(going|heading|time)\b)(?=.*\b(beach|playa)\b).*$', event['text'].lower()):
        client.web_client.chat_postMessage(
            channel=channel,
            text='how about no?',
            attachments=[
                {
                    "fallback": "back to work",
                    "image_url": "https://media2.giphy.com/media/W3Ch3vjHi5FGefDT0G/giphy.gif?cid=ecf05e47z6a9knf03kh82yhhn3sqxq5zj7k2e85nnnmq00ls&rid=giphy.gif&ct=g"
                }
            ]
        )
        return


# Process events
def process(client: SocketModeClient, req: SocketModeRequest):
    if req.type == "events_api":
        # Acknowledge the request anyway
        response = SocketModeResponse(envelope_id=req.envelope_id)
        client.send_socket_mode_response(response)

        # Add a reaction to the message if it's a new message
        if req.payload["event"]["type"] == "message" \
                and req.payload["event"].get("subtype") is None:
            processMessage(req.payload["event"], client)


asyncio.run(main())
