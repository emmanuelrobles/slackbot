class RequestMessage:
    __user_id__: str
    __text__: str
    __channel__: str

    def __init__(self, user_id: str, text: str, channel: str):
        self.__user_id__ = user_id
        self.__text__ = text
        self.__channel__ = channel

    def get_user_id(self):
        return self.__user_id__

    def get_text(self):
        return self.__text__

    def get_channel(self):
        return self.__channel__


class ResponseMessage:
    __text__: str
    __channel__: str
    __attachments__: [(str, str)]

    def __init__(self, text: str, channel: str, __attachments__: [(str, str)]):
        self.__text__ = text
        self.__channel__ = channel
        self.__attachments__ = __attachments__

    def get_text(self):
        return self.__text__

    def get_channel(self):
        return self.__channel__

    def get_attachments(self):
        return self.__attachments__
