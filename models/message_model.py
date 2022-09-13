from importlib.metadata import metadata
from pydantic import BaseModel
from datetime import datetime
from uuid import UUID, uuid4


class MessageMetadata(BaseModel):

    schemaIdentifier: str = "spqr-standard-message-schema"
    schemaVersion: str = "0.0.1"
    messageUuid: UUID = uuid4()
    messageTimestamp: datetime = "2021-10-13T18:13:47.895+02:00"
    messagePublisher: str = "Gravitas"
    messagePublisherEnvironment: str = "dev"


class Payload(BaseModel):

    factSpecificationIdentifier: str = "SPQR-123"
    factValue: int = 99
    factIntervalStart: datetime = "2021-10-13T18:13:00.000+02:00"
    factIntervalEnd: datetime = "2021-10-13T18:14:00.000+02:00"
    pipelineType: str = "stream"
    pipelineEnvironment: str = "dev"
    pipelineIdentifier: str = "Deepsea Salesorder"
    pipelineComponent: str = "Gravitas"
    pipelineComponentType: str = "Gravitas GSA"
    pipelineComponentIdentifier: str = "ov-deepsea-salesorder"


class MessageModel(BaseModel):
    message_metadata: MessageMetadata
    payload: Payload
