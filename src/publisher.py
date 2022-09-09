import os
from google.cloud import pubsub_v1
from support_functions import *
from publish_methodes import *
from keys_to_randomize import keys_to_randomize

config = read_conf()
credentials_path = config["gcpCredentials"]["credentialsPath"]
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path
publisher = pubsub_v1.PublisherClient()
topic_path = config["gcpCredentials"]["topicPath"]
num_of_messages = config["messageParameters"]["numberOfMessages"]


def send_messages():
    data = read_and_radomize(keys_to_randomize)
    if config["batch"]:
        print("trigger batch processing")
        batch_settings = config["batchSettings"]
        publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"], num_of_messages, batch_settings, data
        )
    else:
        publish_messages(topic_path, num_of_messages, data)


send_messages()
