from src.keys_to_randomize import *


def test_keys_to_randomize():

    keys_to_randomize1 = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
    }

    keys_to_randomize2 = {
        "pipelineComponent": gen_random_string(),
        "pipelineName": gen_random_string(),
        "timestampStart": gen_random_date(),
        "timestampStop": gen_random_date(),
    }

    assert keys_to_randomize1 != keys_to_randomize2
