from app.models.domain import PredictionRequest

def predict_severity(payload: PredictionRequest):
    score = min(100, payload.failed_logins * 6 + payload.source_reputation * 0.35 + payload.endpoint_risk * 0.35 + payload.unusual_hour * 12 + payload.malware_indicator * 28)
    if score >= 85:
        severity = "Critical"
    elif score >= 70:
        severity = "High"
    elif score >= 45:
        severity = "Medium"
    else:
        severity = "Low"
    flags = []
    if payload.failed_logins >= 10: flags.append("brute force")
    if payload.unusual_hour: flags.append("unusual login time")
    if payload.endpoint_risk > 70: flags.append("abnormal endpoint activity")
    if payload.source_reputation > 75: flags.append("suspicious IP behavior")
    if payload.malware_indicator: flags.append("malware indicator")
    return {"severity": severity, "risk_score": round(score), "confidence": min(97, 62 + len(flags) * 8), "anomaly_flags": flags, "explanation": "Risk is driven by " + (", ".join(flags) if flags else "normal baseline indicators") + "."}
