from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "PsyScholar AI"
    app_env: str = "development"
    api_prefix: str = "/api/v1"
    openai_api_key: str | None = None
    openalex_email: str | None = None
    database_url: str = "postgresql://postgres:postgres@localhost:5432/psyscholar"
    cors_origins: list[str] = ["http://localhost:3000"]

    model_config = SettingsConfigDict(env_file=".env", env_file_encoding="utf-8")


settings = Settings()
