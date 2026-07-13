from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Knowledge Hub"

    api_prefix: str = "/api"

    secret_key: str

    access_token_expire_minutes: int = 60

    database_url: str

    ollama_base_url: str

    chroma_db_path: str

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()