from src.keys_to_randomize import *


def test_keys_to_randomize():

    keys_to_randomize1 = {
        "pipelineComponent": gen_string(),
        "pipelineName": gen_string(),
        "timestampStart": gen_date(),
        "timestampStop": gen_date(),
    }

    keys_to_randomize2 = {
        "pipelineComponent": gen_string(),
        "pipelineName": gen_string(),
        "timestampStart": gen_date(),
        "timestampStop": gen_date(),
    }

    assert keys_to_randomize1 != keys_to_randomize2
