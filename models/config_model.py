from xmlrpc.client import Boolean
from pydantic import BaseModel


class ConfigParameters(BaseModel):
    numberOfMessages: int = 15
    batch: Boolean = False
    maxMessages: int = 100
    maxBytes: int = 1024
    maxLatency: int = 1
