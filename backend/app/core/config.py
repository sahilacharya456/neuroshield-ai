from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    app_name: str = "NeuroShield AI"
    api_prefix: str = "/api"
    jwt_secret: str = "change-me-in-production"
    jwt_algorithm: str = "HS256"
    jwt_expire_minutes: int = 60
    mongodb_url: str = "mongodb://localhost:27017"
    mongodb_db: str = "neuroshield_ai"
    cors_origins: list[str] = ["http://localhost:5173"]

settings = Settings()
