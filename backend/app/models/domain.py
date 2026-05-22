from pydantic import BaseModel, Field
from typing import List, Optional

class User(BaseModel):
    id: str
    name: str
    email: str
    role: str = "Viewer"
    status: str = "Active"

class Alert(BaseModel):
    id: str
    title: str
    severity: str
    status: str
    source_ip: str
    destination_ip: str = "10.0.0.10"
    endpoint: str
    mitre_technique: str
    risk_score: int
    confidence: int
    explanation: str

class IncidentNote(BaseModel):
    author: str
    body: str
    created_at: str

class Incident(BaseModel):
    id: str
    title: str
    severity: str
    status: str
    assigned_analyst: str
    affected_assets: List[str]
    timeline: List[str]
    remediation: str
    notes: List[IncidentNote] = []

class Endpoint(BaseModel):
    hostname: str
    os: str
    agent_status: str
    health: str
    last_seen: str
    risk_score: int

class IOC(BaseModel):
    id: str
    type: str
    value: str
    status: str
    confidence: int
    linked_incident: Optional[str] = None

class PredictionRequest(BaseModel):
    failed_logins: int = Field(ge=0)
    unusual_hour: int = Field(ge=0, le=1)
    source_reputation: int = Field(ge=0, le=100)
    endpoint_risk: int = Field(ge=0, le=100)
    malware_indicator: int = Field(ge=0, le=1)
