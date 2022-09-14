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
    return "finished"


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
    return "finished"


async def read_query_msg_and_send(data, query_config):
    data = await read_and_randomize(keys_to_randomize, data)
    query_config = json.loads(query_config)
    if query_config["batch"]:
        print("trigger batch processing")
        batch_settings = {
            "maxMessages": query_config["maxMessages"],
            "maxBytes": query_config["maxBytes"],
            "maxLatency": query_config["maxLatency"],
        }
        response = await publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"],
            query_config["numberOfMessages"],
            batch_settings,
            data,
        )
    else:
        response = await publish_messages(
            topic_path, query_config["numberOfMessages"], data
        )
    return response
