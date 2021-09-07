import random

from consts import lines
import helpers


def goodMorningMessage(client,channel):
    client.web_client.chat_postMessage(
        channel=channel,
        text=random.choice(lines.bot_lines_good_morning)
    )


def goodNightMessage(client,channel):
    client.web_client.chat_postMessage(
        channel=channel,
        text=random.choice(lines.bot_lines_good_night)
    )


def noonMessage(client,channel):
    client.web_client.chat_postMessage(
        channel=channel,
        text=random.choice(lines.bot_lines_noon)
    )


def preeStandupMessage(client,channel):
    if helpers.chance(25):
        client.web_client.chat_postMessage(
            channel=channel,
            text=random.choice(lines.bot_lines_pre_standup)
        )

