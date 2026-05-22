import asyncio
from fastapi import APIRouter, Depends, HTTPException, WebSocket, WebSocketDisconnect
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from app.core.config import settings
from app.core.security import create_access_token
from app.models.domain import PredictionRequest
from app.services import ai, store

router = APIRouter()
oauth2 = OAuth2PasswordBearer(tokenUrl="/api/auth/login")

def current_user(token: str = Depends(oauth2)):
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
        return {"email": payload["sub"], "role": payload["role"]}
    except JWTError as exc:
        raise HTTPException(status_code=401, detail="Invalid token") from exc

def require_role(*roles):
    def guard(user=Depends(current_user)):
        if user["role"] not in roles:
            raise HTTPException(status_code=403, detail="Insufficient role")
        return user
    return guard

@router.post("/auth/login")
def login(form: dict):
    email = form.get("email", "admin@neuroshield.ai")
    role = "Viewer" if "viewer" in email else "Analyst" if "analyst" in email else "Admin"
    return {"access_token": create_access_token(email, role), "token_type":"bearer", "user":{"email":email,"role":role,"name":"Sahil Khan" if role=="Admin" else role+" User"}}

@router.post("/auth/register")
def register(form: dict):
    return {"message":"registered", "email": form.get("email"), "role":"Viewer"}

@router.get("/auth/me")
def me(user=Depends(current_user)):
    return user

@router.get("/dashboard")
def dashboard(user=Depends(current_user)):
    return {"total_alerts":1284,"critical_alerts":37,"endpoints":428,"incidents":12,"blocked_ips":186,"malware_indicators":29,"suspicious_logins":74,"trend":[42,55,61,48,79,38,44]}

@router.get("/alerts")
def list_alerts(user=Depends(current_user)):
    return store.alerts

@router.get("/alerts/{alert_id}")
def get_alert(alert_id: str, user=Depends(current_user)):
    return next((a for a in store.alerts if a.id == alert_id), store.alerts[0])

@router.get("/incidents")
def list_incidents(user=Depends(current_user)):
    return store.incidents

@router.get("/incidents/{incident_id}")
def get_incident(incident_id: str, user=Depends(current_user)):
    return next((i for i in store.incidents if i.id == incident_id), store.incidents[0])

@router.post("/incidents")
def create_incident(payload: dict, user=Depends(require_role("Admin", "Analyst"))):
    store.audit_logs.append({"actor": user["email"], "action":"create_incident", "target": payload.get("title"), "result":"success"})
    return {"id":"INC-DEMO", **payload}

@router.get("/endpoints")
def list_endpoints(user=Depends(current_user)):
    return store.endpoints

@router.get("/threat-intel")
def threat_intel(user=Depends(current_user)):
    return store.iocs

@router.get("/mitre")
def mitre(user=Depends(current_user)):
    return store.mitre

@router.post("/ai-predictions/severity")
def severity_prediction(payload: PredictionRequest, user=Depends(current_user)):
    return ai.predict_severity(payload)

@router.post("/reports/incidents/{incident_id}")
def generate_report(incident_id: str, user=Depends(current_user)):
    incident = next((i for i in store.incidents if i.id == incident_id), store.incidents[0])
    markdown = "\n".join([
        f"# Incident Report: {incident.title}",
        "",
        "## Summary",
        f"{incident.severity} incident assigned to {incident.assigned_analyst}.",
        "",
        "## Root Cause",
        "Credential access and anomalous endpoint behavior.",
        "",
        "## Remediation",
        incident.remediation,
        "",
        "## Conclusion",
        "Containment and monitoring are recommended.",
    ])
    return {"incident_id": incident.id, "format":"markdown", "content": markdown}

@router.get("/notifications")
def notifications(user=Depends(current_user)):
    return store.notifications

@router.get("/audit-logs")
def audit_logs(user=Depends(require_role("Admin"))):
    return store.audit_logs

@router.get("/users")
def users(user=Depends(require_role("Admin"))):
    return store.users

@router.websocket("/ws/alerts")
async def alert_socket(websocket: WebSocket):
    await websocket.accept()
    idx = 0
    try:
        while True:
            alert = store.alerts[idx % len(store.alerts)].model_dump()
            await websocket.send_json(alert)
            idx += 1
            await asyncio.sleep(4)
    except WebSocketDisconnect:
        return
