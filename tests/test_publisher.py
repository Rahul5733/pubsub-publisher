from os import read
from src import publisher
from src.support_functions import *
from src.publish_methodes import *
import os
from src.keys_to_randomize import *


def test_read_conf():
    assert read_conf()["gcpCredentials"]["projectId"] == "cloudlab_rso"


async def test_read_and_randomize():
    assert isinstance(await read_and_randomize(keys_to_randomize), bytes)


async def test_publish_messages_with_batch_settings():
    config = read_conf()
    data = await read_and_randomize(keys_to_randomize)
    num_of_messseges = config["messageParameters"]["numberOfMessages"]
    batch_settings = config["batchSettings"]
    assert (
        await publish_messages_with_batch_settings(
            config["gcpCredentials"]["topicPath"],
            num_of_messseges,
            batch_settings,
            data,
        )
        == read_conf()["messageParameters"]["numberOfMessages"] - 1
    )


async def test_publish_messages():
    config = read_conf()
    data = await read_and_randomize(keys_to_randomize)
    num_of_messseges = config["messageParameters"]["numberOfMessages"]
    batch_settings = config["batchSettings"]
    assert (
        await publish_messages(
            config["gcpCredentials"]["topicPath"],
            num_of_messseges,
            data,
        )
        == 16
    )


async def test_read_and_randomize():
    message = await read_message()
    keys_to_randomize1 = {
        "factIntervalStart": gen_random_date(),
        "factIntervalEnd": gen_random_date(),
        "pipelineComponentType": gen_random_string(),
        "pipelineEnvironment": gen_random_string(),
        "pipelineComponentIdentifier": gen_random_string(),
    }
    data_1 = await randomize_message(message, keys_to_randomize1)

    keys_to_randomize2 = {
        "factIntervalStart": gen_random_date(),
        "factIntervalEnd": gen_random_date(),
        "pipelineComponentType": gen_random_string(),
        "pipelineEnvironment": gen_random_string(),
        "pipelineComponentIdentifier": gen_random_string(),
    }
    data_2 = await randomize_message(message, keys_to_randomize2)

    assert data_1 == data_2
