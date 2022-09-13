from src.publisher import send_messages, send_messages_from_query
from models.config_model import ConfigParameters
import asyncio
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
