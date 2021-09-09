import random
from typing import Optional

import helpers
from consts import users, lines
from models.messages import RequestMessage, ResponseMessage, ResponseMessageType


def add_reaction_eyes(message: RequestMessage) -> Optional[ResponseMessage]:
    return ResponseMessage(message_type=ResponseMessageType.REACTION, channel=message.get_channel(), text='eyes', event=message.get_event())


def pierre_response_message(message: RequestMessage) -> Optional[ResponseMessage]:
    return ResponseMessage(message_type=ResponseMessageType.MESSAGE,
                           channel=message.get_channel(),
                           text=(random.choice(lines.bot_lines_pierre))
                           .format(name=users.get_a_name(users.UsersEnums.PIERRE)))
