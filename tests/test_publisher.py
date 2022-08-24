from os import read
from src import publisher
from src.support_functions import *
from src.publish_methodes import *
import os


def test_read_conf():
    assert read_conf()["gcpCredentials"]["projectId"] == "cloudlab_rso"


def test_read_message():
    assert isinstance(read_message(), bytes)


def test_publish_messages_with_batch_settings():
    config = read_conf()
    data = read_message()
    num_of_messseges = config["messageParameters"]["numberOfMessages"]
    batch_settings = config["batchSettings"]
    assert (
        publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"],
            num_of_messseges,
            batch_settings,
            data,
        )
        == read_conf()["messageParameters"]["numberOfMessages"] - 1
    )


def test_publish_messages():
    config = read_conf()
    data = read_message()
    num_of_messseges = config["messageParameters"]["numberOfMessages"]
    batch_settings = config["batchSettings"]
    assert (
        publish_messages(
            config["gcpCredentials"]["topicPath"],
            num_of_messseges,
            data,
        )
        == 16
    )
