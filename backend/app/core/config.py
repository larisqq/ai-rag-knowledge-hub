from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    app_name: str = "AI Knowledge Hub"

    api_prefix: str = "/api"

    secret_key: str

    access_token_expire_minutes: int = 60

    database_url: str

    ollama_base_url: str

    chroma_db_path: str

    ollama_model: str = "llama3.2:3b"

    embedding_model: str = "nomic-embed-text"

    retrieval_results: int = 4

    chunk_size: int = 1000

    chunk_overlap: int = 200
    
    chroma_collection: str = "documents"
    
    upload_folder: str = "app/uploads/pdfs"

    model_config = SettingsConfigDict(
        env_file=".env",
        extra="ignore",
    )


settings = Settings()