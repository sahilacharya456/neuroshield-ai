from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def token():
    res = client.post('/api/auth/login', json={'email':'admin@neuroshield.ai','password':'NeuroShield@123'})
    assert res.status_code == 200
    return res.json()['access_token']

def test_health():
    assert client.get('/health').json()['status'] == 'ok'

def test_alerts_require_auth_and_return_data():
    res = client.get('/api/alerts', headers={'Authorization': f'Bearer {token()}'})
    assert res.status_code == 200
    assert res.json()[0]['id'].startswith('ALT-')

def test_ai_prediction():
    res = client.post('/api/ai-predictions/severity', json={'failed_logins':12,'unusual_hour':1,'source_reputation':86,'endpoint_risk':70,'malware_indicator':0}, headers={'Authorization': f'Bearer {token()}'})
    assert res.status_code == 200
    assert res.json()['severity'] in ['High','Critical']
