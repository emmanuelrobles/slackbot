import re

import messages.bot_message_cases as cases
import messages.bot_messages as bot
from models.messages import RequestMessage


def get_messages(message: RequestMessage) -> [(callable, callable)]:
    message_func = __lazy(message)
    return [

        (message_func(cases.case_add_eye_reaction), message_func(bot.add_reaction_eyes)),
        (message_func(cases.case_pierre_response), message_func(bot.pierre_response_message)),
        (message_func(cases.case_bot_lines), message_func(bot.bot_lines)),
        (message_func(cases.case_shh_line), message_func(bot.shh_line)),
        (message_func(cases.case_cache_fe_line), message_func(bot.cache_line)),
        (message_func(cases.case_beach_line), message_func(bot.beach_line)),
        (message_func(cases.case_picture_mad_line), message_func(bot.bot_pic_mad_line)),
        (message_func(cases.case_bug_found_line), message_func(bot.bug_found_line)),
        (message_func(cases.case_on_fire_line), message_func(bot.on_fire_line)),
    ]


def __lazy(message: RequestMessage):
    def lazy_helper(func):
        def void_func():
            return func(message)

        return void_func

    return lazy_helper

