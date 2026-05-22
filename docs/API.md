# API Documentation

Base URL: http://localhost:8000/api

- POST /auth/login - returns JWT and user profile.
- POST /auth/register - creates a Viewer demo account.
- GET /auth/me - validates JWT.
- GET /dashboard - dashboard metrics.
- GET /alerts and GET /alerts/{id} - alert triage data.
- GET /incidents and GET /incidents/{id} - incident workflow data.
- POST /incidents - Analyst/Admin incident creation.
- GET /endpoints - endpoint health.
- GET /threat-intel - IOC intelligence.
- GET /mitre - MITRE ATT&CK mappings.
- POST /ai-predictions/severity - returns severity, risk score, confidence, anomaly flags, and explanation.
- POST /reports/incidents/{id} - returns generated Markdown report.
- GET /users and /audit-logs - Admin-only endpoints.
- WS /ws/alerts - real-time alert stream.
