# Deployment Guide

## Vercel Frontend

- Set project root to frontend.
- Build command: npm run build.
- Output directory: dist.
- Environment: VITE_API_URL and VITE_WS_URL.

## Render Backend

- Create a Python web service from backend.
- Build command: pip install -r requirements.txt.
- Start command: uvicorn app.main:app --host 0.0.0.0 --port $PORT.
- Set JWT_SECRET, MONGODB_URL, MONGODB_DB, and CORS_ORIGINS.

## MongoDB Atlas

- Create a free cluster.
- Add Render outbound access or 0.0.0.0/0 for demos.
- Store the Atlas connection string in MONGODB_URL.
