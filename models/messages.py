from enum import Enum


class RequestMessage:
    __user_id: str
    __text: str
    __channel: str
    __event: dict

    def __init__(self, user_id: str, text: str, channel: str, event: dict = None):
        self.__user_id = user_id
        self.__text = text
        self.__channel = channel
        self.__event = event

    def get_user_id(self):
        return self.__user_id

    def get_text(self):
        return self.__text

    def get_channel(self):
        return self.__channel

    def get_event(self):
        return self.__event


class ResponseMessageType(Enum):
    MESSAGE = 0
    REACTION = 1


class ResponseMessage:
    __text: str
    __channel: str
    __message_type: ResponseMessageType
    __event: dict
    __attachments: [(str,str)]

    def __init__(self, text: str, channel: str, message_type: ResponseMessageType, event: dict = None,attachments: [(str,str)]=None):
        self.__text = text
        self.__channel = channel
        self.__event = event
        self.__message_type = message_type
        self.__attachments = attachments

    def get_text(self):
        return self.__text

    def get_channel(self):
        return self.__channel

    def get_event(self):
        return self.__event

    def get_message_type(self):
        return self.__message_type

    def get_attachments(self):
        return self.__attachments
