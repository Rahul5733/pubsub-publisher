from random import choice, random
import string
from typing import Dict, List
import time, datetime, asyncio


@asyncio.coroutine
def gen_random_string(length=18, chars=string.ascii_letters):
    return "".join([choice(chars) for i in range(length)])


@asyncio.coroutine
def gen_random_digits(length=4, chars=string.digits):
    return int("".join([choice(chars) for i in range(length)]))


@asyncio.coroutine
def gen_random_date():
    ts = time.time()
    rand_nums = gen_random_digits()
    return str(
        datetime.datetime.fromtimestamp(ts).strftime(
            "%Y-%m-%dT%H:%M:%S.{}+02:00".format(str(rand_nums))
        )
    )


keys_to_randomize = {
    "pipelineComponent": gen_random_string(),
    "pipelineName": gen_random_string(),
    "timestampStart": gen_random_date(),
    "timestampStop": gen_random_date(),
}
