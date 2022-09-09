from random import choice, random
import string
from typing import Dict, List


def gen_string(length=18, chars=string.ascii_letters):
    return "".join([choice(chars) for i in range(length)])


def randomize_key_values(keys: List) -> Dict:
    # for key in keys:
    pass
