import yaml
import json


def read_conf():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
        return data


def read_message():
    with open("message.json") as f:
        data = json.load(f)
        return data


def randomize_message(data, keys_to_randomize):
    for key in keys_to_randomize.keys():
        data[key] = keys_to_randomize[key]
    return data


def read_and_radomize(keys_to_randomize):
    message = read_message()
    message = randomize_message(message, keys_to_randomize)
    return str(message).encode("utf-8")
