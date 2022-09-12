from src.publisher import send_messages
import asyncio
from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def main():
    r = await send_messages()
    return r
