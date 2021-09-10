import random

from consts import lines
from models.messages import ResponseMessage, ResponseMessageType


def good_morning_message(channel: str) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=channel,
                           text=random.choice(lines.bot_lines_good_morning)
                           )


def good_night_message(channel: str) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=channel,
                           text=random.choice(lines.bot_lines_good_night)
                           )


def noon_message(channel: str) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=channel,
                           text=random.choice(lines.bot_lines_noon)
                           )


def pre_stand_up_message(channel: str) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=channel,
                           text=random.choice(lines.bot_lines_pre_standup)
                           )


def good_morning_hall_pass_message(channel: str) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=channel,
                           text=random.choice(lines.bot_lines_hall_pass),
                           attachments=[
                               {
                                   "fallback": "hall-pass",
                                   "image_url": "https://i.postimg.cc/Jn4sg4wM/hall-pass-pad-032-28472-1593602826-1.png"
                               }
                           ]
                           )
