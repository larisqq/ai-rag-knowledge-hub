from langchain_ollama import OllamaEmbeddings


class EmbeddingService:
    """
    Responsible for generating vector embeddings
    using Ollama's nomic-embed-text model.
    """

    def __init__(self):
        self.model = OllamaEmbeddings(
            model="nomic-embed-text"
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