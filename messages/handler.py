import os
from typing import Optional

import rx
import schedule
from rx import Observable
from rx import operators as ops
from rx.subject import Subject

import helpers
import messages.bot_scheduled_messages as bot_scheduled
from messages.messages_map import get_messages
from models.messages import RequestMessage, ResponseMessage


def message_handler(observable: Observable):
    schedule_msg = __schedule_messages()
    return rx.merge(
        observable.pipe(
            ops.map(lambda msg: __handle(msg)),
        ),
        schedule_msg
    ).pipe(
        ops.filter(lambda res: res is not None)
    )


# handle schedule messages
def __schedule_messages() -> Observable:
    subject = Subject()
    channel = os.environ['CHANNEL']

    # always run the schedule msg
    def always():
        return lambda: True

    # run it give it a chance
    def chance(p: int):
        return lambda: helpers.chance(p)

    # dispatch a given message with a consistency
    def __dispatch_message(func, consistency):
        return lambda: subject.on_next(func(channel)) if consistency() else None

    # run the jobs only the weekdays
    def __weekday_job(x, t=None):
        from datetime import datetime
        week = datetime.today().weekday()
        if t is not None and week < 5:
            schedule.every().day.at(t).do(x)

    # jobs
    __weekday_job(__dispatch_message(bot_scheduled.good_morning_message, always()), '07:00')
    __weekday_job(__dispatch_message(bot_scheduled.good_morning_hall_pass_message, chance(100)), '07:01')
    __weekday_job(__dispatch_message(bot_scheduled.pre_stand_up_message, chance(50)), '10:30')
    __weekday_job(__dispatch_message(bot_scheduled.noon_message, always()), '12:00')
    __weekday_job(__dispatch_message(bot_scheduled.good_night_message, always()), '18:00')

    return subject


# handle incoming messages
def __handle(message: RequestMessage) -> Optional[ResponseMessage]:
    messages = get_messages(message)
    for tuple_func_bool_func in messages:
        if tuple_func_bool_func[0]():
            return tuple_func_bool_func[1]()
