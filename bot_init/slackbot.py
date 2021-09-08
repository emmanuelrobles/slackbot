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
from models.requestmessage import RequestMessage


def slack_bot_init() -> rx.Observable:
    # load env
    env_path = Path('.') / '.env'
    load_dotenv(dotenv_path=env_path)

    # client setup
    client = SocketModeClient(
        app_token=os.environ['APP_TOKEN'],
        web_client=WebClient(os.environ['WEB_CLIENT_TOKEN'])
    )

    # Subject to handle all messages
    slack_response_subject = rx.subject.Subject()

    client.socket_mode_request_listeners.append(lambda client, req: process(client, req, slack_response_subject))
    client.connect()

    # setup the observable
    return setup_subject(client,slack_response_subject)


# Process events
def process(client: SocketModeClient, req: SocketModeRequest, slack_response_subject):
    message = namedtuple('message', ['client', 'request'])
    slack_response_subject.on_next(message(client, req))


def setup_subject(client, slack_response_subject):
    def acknowledge_message(msg):
        response = SocketModeResponse(envelope_id=msg.request.envelope_id)
        client.send_socket_mode_response(response)

    return slack_response_subject.pipe(
        ops.filter(lambda msg:
                   msg.request.type == 'events_api'),
        ops.do_action(lambda msg: acknowledge_message(msg)),
        ops.filter(lambda msg: msg.request.payload["event"]["type"] == "message" and msg.request.payload["event"].get(
            "subtype") is None),
        ops.map(lambda msg: RequestMessage(msg.request.payload["event"]["user"], msg.request.payload["event"]["text"],
                                           msg.request.payload["event"]["channel"]))
    )
