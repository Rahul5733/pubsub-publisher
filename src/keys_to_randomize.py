from random import choice, random
import string
from typing import Dict, List
import time, asyncio, pytz
from datetime import datetime


def gen_random_string(length=18, chars=string.ascii_letters):
    return "".join([choice(chars) for i in range(length)])


def gen_random_digits(length=4, chars=string.digits):
    return int("".join([choice(chars) for i in range(length)]))


def gen_random_date():
    d = datetime.utcnow().replace(tzinfo=pytz.utc)
    return d.isoformat()


keys_to_randomize = {
    "factIntervalStart": gen_random_date(),
    "factIntervalEnd": gen_random_date(),
    "pipelineComponentType": gen_random_string(),
    "pipelineEnvironment": gen_random_string(),
    "pipelineComponentIdentifier": gen_random_string(),
}
