from src.publisher import (
    send_messages,
    send_messages_from_query,
    read_query_msg_and_send,
)
from models.config_model import ConfigParameters
from models.message_model import MessageModel
from src.tags_metadata import tags_metadata
from fastapi import FastAPI


app = FastAPI(openapi_tags=tags_metadata)


@app.get("/", tags=["Send Message Command"])
async def main():
    r = await send_messages()
    return {"process status: ": r}


@app.post("/", tags=["Post Config and Send Message"])
async def send_msg_with_query_config(parameters: ConfigParameters):
    print(parameters.maxMessages)
    r = await send_messages_from_query(parameters)
    return {"process status: ": r}


@app.post("/sendmsg", tags=["Post Message via Query"])
async def send_msg_with_query_msg(message_data: MessageModel, config: ConfigParameters):
    r = await read_query_msg_and_send(message_data.json(), config.json())
    return {"process status: ": r}


@app.get("/test", tags=["test"])
async def read_main():
    return {"msg": "Hello World"}
