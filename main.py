from email import message
from src.publisher import (
    send_messages,
    send_messages_from_query,
    read_query_msg_and_send,
)
from models.config_model import ConfigParameters
from models.message_model import MessageModel
import asyncio, json
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    r = await send_messages()
    return r


@app.post("/")
async def read_query_and_send(parameters: ConfigParameters):
    print(parameters.maxMessages)
    r = await send_messages_from_query(parameters)
    return r


@app.post("/sendmsg")
async def query_message(message_data: MessageModel):
    r = await read_query_msg_and_send(message_data.json())
    return r
