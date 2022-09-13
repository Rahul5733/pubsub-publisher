import yaml
import json
import asyncio


def read_conf():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
        return data


@asyncio.coroutine
def read_message():
    with open("message.json") as f:
        data = json.load(f)
        return data


@asyncio.coroutine
def randomize_message(data, keys_to_randomize):
    for key in keys_to_randomize.keys():
        data["payload"][key] = keys_to_randomize[key]
    return data


async def read_and_randomize(keys_to_randomize, *message) -> dict:

    if not message:
        message = await read_message()
        message = json.dumps(message).encode("utf-8")
        return message
    message = json.loads(message[0])
    message = await randomize_message(message, keys_to_randomize)
    # convert dict to bytestring
    message = json.dumps(message).encode("utf-8")
    return message
