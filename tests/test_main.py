import pytest
from httpx import AsyncClient
from fastapi.testclient import TestClient
from main import app
from src.support_functions import *
from src.publish_methodes import *
from src.keys_to_randomize import *


client = TestClient(app)


def test_read_main():
    response = client.get("/test")
    assert response.status_code == 200
    assert response.json() == {"msg": "Hello World"}


def test_sendmsg():
    response = client.get("/")
    assert response.status_code == 200


def test_read_query_and_send():
    config = {
        "numberOfMessages": 15,
        "batch": False,
        "maxMessages": 100,
        "maxBytes": 1024,
        "maxLatency": 1,
    }

    response = client.post(
        "/",
        headers={"X-Token": "coneofsilence"},
        json=config,
    )
    assert response.status_code == 200


async def test_sendmsg():
    with open("./tests/test_data.json") as f:
        data = json.load(f)

    response = client.post("/sendmsg", headers={"X-Token": "coneofsilence"}, json=data)
    assert response.status_code == 200
