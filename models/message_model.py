from pydantic import BaseModel, Field
from datetime import datetime
from uuid import UUID, uuid4


class MessageMetadata(BaseModel):

    schemaIdentifier: str = Field(
        default="spqr-standard-message-schema",
        description="Name des verwendeten / relevante Schemas. hier: 'spqr-standard-message-schema'",
    )
    schemaVersion: str = Field(
        default="0.0.1",
        description="Version des Schema (semantische Versionierung!?)",
    )
    messageUuid: UUID = uuid4()
    messageTimestamp: datetime = Field(
        default="2021-10-13T18:13:47.895+02:00",
        description="RFC-3339 konformer Zeitstempel mit UTC-Zeitzone, Nachkommastellen der Sekunden(?): min. 3",
    )
    messagePublisher: str = Field(
        default="Gravitas",
        description="sendendes System bzw. sendende Komponente bspw. Gravitas? oder auch 'Gravitas ADS'? Oder auch Source-System 'OneContact'? Für Problemsuche mit eintreffenden Nachrichten.",
    )
    messagePublisherEnvironment: str = Field(
        default="dev",
        description="'klassische Unterteilung' DEV, TEST, PROD. Potentiell mit bewusster Redundanz zu Informationen an den gemeldeten Fakten.",
    )


class Payload(BaseModel):

    factSpecificationIdentifier: str = Field(
        default="SPQR-123",
        description="Referenz auf eine SPQR-Fact-Definition in der Fakt Definitionen ( -> factDefinitions.identifier), welche wiederum auf der KPI-Liste vx.x.x basiert.",
    )
    factValue: int = Field(
        default=99,
        description="je nach Definition: ganze Zahlen, Decimalzahlen, Status-Code (Zahl, String, Boolean, ...), (Frei-)Text. TODO: Liste der erlaubten Ausprägungen.",
    )
    factIntervalStart: datetime = Field(
        default="2021-10-13T18:13:00.000+02:00",
        description="Zeitstempel RFC-3339 (bevorzugt UTC)",
    )
    factIntervalEnd: datetime = Field(
        default="2021-10-13T18:13:00.000+02:00",
        description="Zeitstempel RFC-3339 (bevorzugt UTC). Im Fall von Einzelevents: a) entfällt oder b) End := Start (:= Dauer 0) ",
    )
    pipelineType: str = Field(
        default="stream",
        description="Unterscheidung nach 'batch' (Bulk), 'stream'. (denkbare Erweiterungen: realtime / neartime?)",
    )
    pipelineEnvironment: str = Field(
        default="dev",
        description="'klassische Unterteilung' DEV, TEST, PROD. Redundant zu messageMetadata.eventPublisherEnvironment. Für Verprobung aufgenommen: potentiell Vereinfachung der Verarbeitung.",
    )
    pipelineIdentifier: str = Field(
        default="Deepsea Salesorder",
        description="eindeutiger Name der Data Pipeline / des Data Products (nicht nur der Regel in Gravitas: hierfür siehe pipelineComponentIdentifier). Erster Anker in das Data Product (data pipeline)",
    )
    pipelineComponent: str = Field(
        default="Gravitas",
        description="""Einordnung der Komponente in der SPQR Referenzarchitektur für Data Pipelines

    # -> Flughöhe: https://blueforte.sharepoint.com/:u:/r/sites/IntentionOTTO1048ClearSight/Freigegebene%20Dokumente/General/SPQR-Logische-Darstellung-Prozess-KPI-Messung-Streaming.drawio.svg?csf=1&web=1&e=3wYRdH
    
    # derzeit nach 4 Komponenten unterschieden: keine eigenen Werte!! Nur die von SPQR Freigegebenen.""",
    )
    pipelineComponentType: str = Field(
        default="Gravitas GSA",
        description="Type der Komponente bspw. Gravitas, Gravitas ADS, DataLake, ... (Name als Label, wie an der Pipeline-Impl. hinterlegt?)",
    )
    pipelineComponentIdentifier: str = Field(
        default="ov-deepsea-salesorder",
        description="je nach Komponente im Solution Design der Data Pipeline, bspw. für Gravitas 'tokenizer' oder Data Set Namen? DV Tabellenname?",
    )


class MessageModel(BaseModel):
    message_metadata: MessageMetadata
    payload: Payload
