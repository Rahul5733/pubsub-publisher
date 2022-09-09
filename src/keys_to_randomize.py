from random import choice, random
import string
from typing import Dict, List
import time, datetime


def gen_string(length=18, chars=string.ascii_letters):
    return "".join([choice(chars) for i in range(length)])


def gen_digits(length=4, chars=string.digits):
    return "".join([choice(chars) for i in range(length)])


def gen_date():
    ts = time.time()
    rand_nums = gen_digits()
    return str(
        datetime.datetime.fromtimestamp(ts).strftime(
            "%Y-%m-%dT%H:%M:%S.{}+02:00".format(rand_nums)
        )
    )


keys_to_randomize = {
    "pipelineComponent": gen_string(),
    "pipelineName": gen_string(),
    "timestampStart": gen_date(),
    "timestampStop": gen_date(),
}
