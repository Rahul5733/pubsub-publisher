import os
from google.cloud import pubsub_v1
from support_functions import *
from publish_methodes import *
from keys_to_randomize import keys_to_randomize
import json

config = read_conf()
credentials_path = config["gcpCredentials"]["credentialsPath"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
publisher = pubsub_v1.PublisherClient()
topic_path = config["gcpCredentials"]["topicPath"]
num_of_messages = config["messageParameters"]["numberOfMessages"]


async def send_messages():
    data = await read_and_randomize(keys_to_randomize)
    if config["batch"]:
        print("trigger batch processing")
        batch_settings = config["batchSettings"]
        publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"], num_of_messages, batch_settings, data
        )
    else:
        await publish_messages(topic_path, num_of_messages, data)


async def send_messages_from_query(parameters):
    data = await read_and_randomize(keys_to_randomize)
    if parameters.batch:
        print("trigger batch processing")
        batch_settings = {
            parameters.maxMessages,
            parameters.maxBytes,
            parameters.maxLatency,
        }
        publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"],
            parameters.numberOfMessages,
            batch_settings,
            data,
        )
    else:
        await publish_messages(topic_path, parameters.numberOfMessages, data)


async def read_query_msg_and_send(data):
    data = await read_and_randomize(keys_to_randomize, data)

    if config["batch"]:
        print("trigger batch processing")
        batch_settings = config["batchSettings"]
        publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"], num_of_messages, batch_settings, data
        )
    else:
        await publish_messages(topic_path, num_of_messages, data)
