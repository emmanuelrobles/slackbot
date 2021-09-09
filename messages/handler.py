import re
from typing import Optional

from rx import Observable
from rx import operators as ops
from messages.messages_map import get_messages
from models.messages import RequestMessage, ResponseMessage


def message_handler(observable: Observable):
    return observable.pipe(
        ops.map(lambda msg: __handle(msg)),
        ops.filter(lambda res: res is not None)
    )


def __handle(message: RequestMessage) -> Optional[ResponseMessage]:
    messages = get_messages(message)
    for val in messages:
        if val[0]:
            return val[1]()
