import os
from collections import namedtuple
from pathlib import Path

import rx
from dotenv import load_dotenv
from slack_sdk.socket_mode import SocketModeClient
from slack_sdk.web import WebClient
from slack_sdk.socket_mode.response import SocketModeResponse
from slack_sdk.socket_mode.request import SocketModeRequest
from rx import operators as ops
import rx.subject
from models.messages import RequestMessage, ResponseMessage, ResponseMessageType


class Slackbot:
    client: SocketModeClient
    # Subject to handle all messages
    __slack_response_subject = rx.subject.Subject

    def __init__(self):
        # load env
        env_path = Path('.') / '.env'
        load_dotenv(dotenv_path=env_path)

        # client setup
        self.client = SocketModeClient(
            app_token=os.environ['APP_TOKEN'],
            web_client=WebClient(os.environ['WEB_CLIENT_TOKEN'])
        )

        # Subject to handle all messages
        self.slack_response_subject = rx.subject.Subject()

        self.client.socket_mode_request_listeners.append(self.__process)
        self.client.connect()

    # Process events
    def __process(self, client: SocketModeClient, req: SocketModeRequest):
        message = namedtuple('message', ['client', 'request'])
        self.slack_response_subject.on_next(message(client, req))

    def get_stream(self):
        def acknowledge_message(msg):
            response = SocketModeResponse(envelope_id=msg.request.envelope_id)
            self.client.send_socket_mode_response(response)

        return self.slack_response_subject.pipe(
            ops.filter(lambda msg:
                       msg.request.type == 'events_api'),
            ops.do_action(lambda msg: acknowledge_message(msg)),
            ops.filter(
                lambda msg: msg.request.payload["event"]["type"] == "message" and msg.request.payload["event"].get(
                    "subtype") is None),
            ops.map(
                lambda msg: RequestMessage(msg.request.payload["event"]["user"], msg.request.payload["event"]["text"],
                                           msg.request.payload["event"]["channel"], event=msg.request.payload["event"]))
        )

    def send_message(self, response: ResponseMessage):
        if response.get_message_type() == ResponseMessageType.REACTION:
            self.client.web_client.reactions_add(
                name="eyes",
                channel=response.get_channel(),
                timestamp=response.get_event()["ts"]
            )
        elif response.get_message_type() == ResponseMessageType.MESSAGE:
            self.client.web_client.chat_postMessage(
                channel=response.get_channel(),
                text=response.get_text(),
                attachments=response.get_attachments()
            )
