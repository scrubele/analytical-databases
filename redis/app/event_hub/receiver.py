import asyncio
# from app import app
# from config import Config

from azure.eventhub import EventHubConsumerClient

class Config(object):
    EVENT_HUB_CONNNECTION_STRING = "Endpoint=sb://lab6-iot.servicebus.windows.net/;SharedAccessKeyName=els;SharedAccessKey=Kb/7PrWYYdqzjMpE/i49rvJvD9Yy0gjzSKYQ90wwThs=;EntityPath=redis-event"
    EVENT_HUB_NAME = "redis-event"
    CONSUMER_GROUP = "$Default"

    
client = EventHubConsumerClient.from_connection_string(
    Config.EVENT_HUB_CONNNECTION_STRING, Config.CONSUMER_GROUP, eventhub_name=Config.EVENT_HUB_NAME)


def on_event(partition_context, event):
    from app.loggers import context
    # context.do_logging("ID: {} Message: {}".format(
    #     partition_context.partition_id, event.body_as_str(encoding='UTF-8')))
    partition_context.update_checkpoint(event)


def receive_data():
    with client:
        client.receive(
            on_event=on_event,
            # "-1" is from the beginning of the partition.
            starting_position="-1",
        )


receive_data()
