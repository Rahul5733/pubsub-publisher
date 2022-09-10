from os import read
from src import publisher
from src.support_functions import *
from src.publish_methodes import *
import os
from keys_to_randomize import *


def test_read_conf():
    assert read_conf()["gcpCredentials"]["projectId"] == "cloudlab_rso"


def test_read_and_randomize():
    assert isinstance(read_and_radomize(), bytes)


def test_publish_messages_with_batch_settings():
    config = read_conf()
    data = read_and_radomize(keys_to_randomize)
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
    data = read_and_radomize(keys_to_randomize)
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


def test_read_and_randomize():
    message = read_message()
    keys_to_randomize1 = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
    }
    data_1 = randomize_message(message, keys_to_randomize1).copy()

    keys_to_randomize2 = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
    }
    data_2 = randomize_message(message, keys_to_randomize2).copy()

    for key in keys_to_randomize:
        assert data_1[key] != data_2[key]
