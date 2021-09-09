import re
from re import Pattern

import helpers
from consts.users import UsersEnums
from messages.messages import add_reaction_eyes, pierre_response_message
from models.messages import RequestMessage


def get_messages(message: RequestMessage) -> [(bool, callable)]:
    message_func = lazy(message)
    return [
        (bool(is_regex_match(r'\b(pierre)\b', message.get_text())) and
         (not is_from_user(message, UsersEnums.SLACKBOT)) and
         helpers.chance(50), message_func(add_reaction_eyes)),

        (is_from_user(message, UsersEnums.PIERRE)
         and helpers.chance(5), message_func(pierre_response_message))
    ]


def is_regex_match(pattern: str, text: str):
    return re.match(pattern, text, re.IGNORECASE)


def is_from_user(message: RequestMessage, user_id: str) -> bool:
    return message.get_user_id() == user_id


def lazy(message: RequestMessage):
    def lazy_helper(func):
        def void_func():
            return func(message)

        return void_func

    return lazy_helper
