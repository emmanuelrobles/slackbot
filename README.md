# Just another SlackBot

## How to set up

1. Create an ```.env``` file
2. in there add ```APP_TOKEN```, ```WEB_CLIENT_TOKEN``` and ```CHANNEL```, keep in mind that it uses ```dotenv``` to read the env variables


## How it works

In the ```bot_init``` file tou will find a bot implementation, with 2 main methods **get_stream** 
and **send_message**, get stream will return an [Observable](http://reactivex.io/documentation/observable.html)
and the app will handle the message, the last thing it does is to call **send_message**

### Message handling
We have a **handler** in ``messages/handler`` that will handle all incoming and scheduled messages

**messages_map** contains a list of tuples, ``(() -> bool,() -> ResponseMessage)`` with all the responses 
that matches a given query (regex)

**bot_messages_cases** **bot_messages** contain the function to build the messages map

### Workflow diagram
![workflow schema](https://i.ibb.co/JQCY6n8/Untitled-Diagram-drawio-1.png)