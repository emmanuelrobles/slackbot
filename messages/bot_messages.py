import random
from consts import users, lines
from models.messages import RequestMessage, ResponseMessage, ResponseMessageType


def add_reaction_eyes(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.REACTION, channel=message.get_channel(), text='eyes',
                           event=message.get_event())


def pierre_response_message(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=(random.choice(lines.bot_lines_pierre))
                           .format(name=users.get_a_name(users.UsersEnums.PIERRE)))


def bot_lines(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(lines.bot_lines)
                           )


def shh_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(lines.bot_lines_shh),
                           attachments=[
                               {
                                   "fallback": ":)",
                                   "image_url": "https://media4.giphy.com/media/EKDIMDsRX3ihy/giphy.gif?cid"
                                                "=ecf05e47qjya842xz1a1lgv6kuk7h039bb0ak9qijue227gi&rid=giphy.gif&ct=g "
                               }
                           ])


def cache_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(
                               lines.bot_lines_cache.format(name=users.get_a_name(message.get_user_id()))),
                           attachments=[
                               {
                                   "fallback": ":)",
                                   "image_url": "https://media0.giphy.com/media/8wb5IPi03CM1gzjWm6/giphy.gif?cid"
                                                "=790b76110caa0045ebd55d910d5ffc79502c741300864090&rid=giphy.gif&ct=g "
                               }
                           ])


def beach_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(
                               lines.bot_lines_beach.format(name=users.get_a_name(message.get_user_id()))),
                           attachments=[
                               {
                                   "fallback": "back to work",
                                   "image_url": "https://media2.giphy.com/media/W3Ch3vjHi5FGefDT0G/giphy.gif?cid"
                                                "=ecf05e47z6a9knf03kh82yhhn3sqxq5zj7k2e85nnnmq00ls&rid=giphy.gif&ct=g "
                               }
                           ])


def bot_pic_mad_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(
                               lines.bot_lines_hate_pic).format(name=users.get_a_name(message.get_user_id()))
                           )


def bug_found_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(
                               lines.bot_lines_bugs).format(name=users.get_a_name(message.get_user_id()))
                           )


def on_fire_line(message: RequestMessage) -> ResponseMessage:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=random.choice(lines.bot_lines_fire).format(
                               name=users.get_a_name(message.get_user_id())),
                           attachments=[
                               {
                                   "fallback": "fire",
                                   "image_url": "https://media0.giphy.com/media/9M5jK4GXmD5o1irGrF/giphy.gif?cid"
                                                "=ecf05e47td2z01plekh551t52xz2sefwximdhqmvcd1e4iae&rid=giphy.gif&ct=g "
                               }
                           ]
                           )


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


