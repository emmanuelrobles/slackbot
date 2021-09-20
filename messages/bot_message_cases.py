import re

import helpers
from consts.users import UsersEnums
from models.messages import RequestMessage


def __is_regex_search(pattern: str, text: str):
    return re.search(pattern=pattern, string=text, flags=re.IGNORECASE)


def __is_from_user(message: RequestMessage, user_id: str) -> bool:
    return message.get_user_id() == user_id


def case_add_eye_reaction(message: RequestMessage) -> bool:
    return (bool(__is_regex_search(r'\b(pierre)\b', message.get_text())) and
            (not __is_from_user(message, UsersEnums.SLACKBOT)) and
            helpers.chance(50))


def case_pierre_response(message: RequestMessage) -> bool:
    return (__is_from_user(message, UsersEnums.PIERRE)
            and helpers.chance(5))


def case_bot_lines(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'\b(costco|jason|bowers)\b', message.get_text()))


def case_shh_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'\bshhh*\b', message.get_text()))


def case_cache_fe_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'^(?=.*\b(cache|add|put)\b)(?=.*\b(frontend|front end|fe)\b).*$'
                                  , message.get_text()))


def case_beach_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'^(?=.*\b(going|heading|time)\b)(?=.*\b(beach|playa)\b).*$', message.get_text()))


def case_picture_mad_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'(:bowers:)', message.get_text()))


def case_bug_found_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'^(?=.*\b(found|new)\b)(?=.*\b(bug|error)\b).*$', message.get_text()))


def case_on_fire_line(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'^(?=.*\b(all|everything|this shit)\b)(?=.*\b(fire|bad)\b).*$', message.get_text()))


def case_ck_wisdom(message: RequestMessage) -> bool:
    return bool(__is_regex_search(r'^(?=.*\b(ck|cornelius)\b)(?=.*\b(wisdom|knowledge)\b).*$', message.get_text()))
