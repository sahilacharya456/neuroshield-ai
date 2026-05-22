# NeuroShield AI

NeuroShield AI is a portfolio-level AI-powered SOC/XDR threat monitoring platform built with React, Vite, Tailwind CSS, Framer Motion, Recharts, Lucide Icons, FastAPI, Python, MongoDB, JWT auth, WebSockets, Scikit-learn, and Docker.

## Features

- Premium dark cybersecurity SaaS interface with animated navigation, glassmorphism panels, neon cyber accents, live feed animations, and responsive dashboards.
- JWT authentication model with Admin, Analyst, and Viewer roles.
- Real-time alert streaming over WebSockets.
- Alert triage with severity, status, source IP, endpoint, AI risk score, confidence, and explanation.
- Scikit-learn AI engine design using Random Forest severity prediction and Isolation Forest anomaly detection.
- MITRE ATT&CK mapping for brute force, PowerShell, valid accounts, and malware execution behaviors.
- Incident management with assignment, timeline, affected assets, remediation, notes, and generated reports.
- Threat intelligence for IPs, domains, hashes, IOC status, history, and incident linking.
- Endpoint health monitoring, admin analytics, audit logs, notification placeholders, and report export endpoints.

## Demo Credentials

- Admin: admin@neuroshield.ai / NeuroShield@123
- Analyst: analyst@neuroshield.ai / NeuroShield@123
- Viewer: viewer@neuroshield.ai / NeuroShield@123

## Quick Start

### Frontend

```bash
cd frontend
npm install
npm run dev
```

Open http://localhost:5173.

### Backend

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://localhost:8000/docs.

### Docker

```bash
docker compose up --build
```

Docker files are included; Docker Desktop must be installed separately.

## Project Structure

```text
frontend/       React/Vite dashboard UI
backend/        FastAPI API, auth, RBAC, WebSockets, services
ai-engine/      Scikit-learn model training script
sample-data/    Training and seed data
docs/           Install, API, deployment, resume docs
docker/         Dockerfiles
screenshots/    Placeholder for project screenshots
```
