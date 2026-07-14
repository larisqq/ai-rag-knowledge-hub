from langchain_ollama import OllamaEmbeddings
from app.core.config import settings


class EmbeddingService:
    """
    Responsible for generating vector embeddings
    using Ollama's nomic-embed-text model.
    """

    def __init__(self):
        self.model = OllamaEmbeddings(
            model=settings.embedding_model,
            base_url=settings.ollama_base_url
        )

    def embed_documents(self, texts: list[str]) -> list[list[float]]:
        """
        Generate embeddings for multiple text chunks.
        """
        return self.model.embed_documents(texts)

    def embed_query(self, query: str) -> list[float]:
        """
        Generate embedding for a user query.
        """
        return self.model.embed_query(query)


embedding_service = EmbeddingService()