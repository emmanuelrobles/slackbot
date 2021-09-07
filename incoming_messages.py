import random
import re

import helpers
from consts import lines
from consts import users


# respond to a message from pierre
def pierre_messages(event: dict, client):
    # if the message is from Pierre's user
    is_from_pierre = event['user'] == 'U02DYBFSED6'

    import helpers
    if is_from_pierre and helpers.chance(5):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text=(random.choice(lines.bot_lines_pierre)).format(name=users.get_a_name('U02DYBFSED6')))


# react to a message with pierre in it
def eye_reaction_message(event: dict, client):
    is_from_bot = event['user'] != 'U02CUDGHJ0P'

    if re.match(r'\b(pierre)\b', event['text'], re.IGNORECASE) and \
            is_from_bot and \
            helpers.chance(50):
        client.web_client.reactions_add(
            name="eyes",
            channel=event["channel"],
            timestamp=event["ts"]
        )


# lines when someone mention jason
def costco_lines(event: dict, client):
    if re.match(r'\b(costco|jason|bowers)\b', event['text'], re.IGNORECASE):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text=random.choice(lines.bot_lines)
        )


# show shhh emoji
def shhh_line(event: dict, client):
    if re.match(r'\bshhh*\b', event['text'], re.IGNORECASE):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text=random.choice(lines.bot_lines_shh),
            attachments=[
                {
                    "fallback": ":)",
                    "image_url": "https://media4.giphy.com/media/EKDIMDsRX3ihy/giphy.gif?cid=ecf05e47qjya842xz1a1lgv6kuk7h039bb0ak9qijue227gi&rid=giphy.gif&ct=g"
                }
            ]
        )


# cache on the FE emoji
def cache_emoji(event: dict, client):
    if re.match(r'^(?=.*\b(cache|add|put)\b)(?=.*\b(frontend|front end|fe)\b).*$', event['text'], re.IGNORECASE):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text='yea, lets put it there',
            attachments=[
                {
                    "fallback": ":)",
                    "image_url": "https://media0.giphy.com/media/8wb5IPi03CM1gzjWm6/giphy.gif?cid"
                                 "=790b76110caa0045ebd55d910d5ffc79502c741300864090&rid=giphy.gif&ct=g "
                }
            ]
        )


# beach_emoji
def beach_emoji(event: dict, client):
    if re.match(r'^(?=.*\b(going|heading|time)\b)(?=.*\b(beach|playa)\b).*$', event['text'], re.IGNORECASE):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text='how about no?',
            attachments=[
                {
                    "fallback": "back to work",
                    "image_url": "https://media2.giphy.com/media/W3Ch3vjHi5FGefDT0G/giphy.gif?cid"
                                 "=ecf05e47z6a9knf03kh82yhhn3sqxq5zj7k2e85nnnmq00ls&rid=giphy.gif&ct=g "
                }
            ]
        )


# reaction to picture
def pic_mad_reaction(event: dict, client):
    if re.match(r'(:bowers:)', event['text'], re.IGNORECASE):
        client.web_client.chat_postMessage(
            channel=event["channel"],
            text=random.choice(lines.bot_lines_hate_pic).format(name=users.get_a_name(event['user']))
        )
