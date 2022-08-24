import os
from google.cloud import pubsub_v1
import yaml
import json
from concurrent import futures


def read_conf():
    with open("config.yaml") as f:
        data = yaml.safe_load(f)
        return data


def read_message():
    with open("message.json") as f:
        data = str(json.load(f))
        return data.encode("utf-8")
