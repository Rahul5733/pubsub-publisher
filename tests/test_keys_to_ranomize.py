from src.keys_to_randomize import *


def test_keys_to_randomize():

    keys_to_randomize1 = {
        "factIntervalStart": gen_random_date(),
        "factIntervalEnd": gen_random_date(),
        "pipelineComponentType": gen_random_string(),
        "pipelineEnvironment": gen_random_string(),
        "pipelineComponentIdentifier": gen_random_string(),
    }

    keys_to_randomize2 = {
        "factIntervalStart": gen_random_date(),
        "factIntervalEnd": gen_random_date(),
        "pipelineComponentType": gen_random_string(),
        "pipelineEnvironment": gen_random_string(),
        "pipelineComponentIdentifier": gen_random_string(),
    }

    assert keys_to_randomize1 != keys_to_randomize2
