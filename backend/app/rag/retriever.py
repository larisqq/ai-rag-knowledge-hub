from app.core.config import settings
from app.rag.embeddings import embedding_service
from app.rag.vector_store import vector_store


class Retriever:
    """
    Retrieves the most relevant document chunks from ChromaDB.
    """

    @staticmethod
    def search(
        query: str,
        n_results: int = settings.retrieval_results,
    ):
        """
        Search the vector database for the most relevant chunks.
        """

        print("Generating query embedding...")

        query_embedding = embedding_service.embed_query(query)

        print("Searching ChromaDB...")

        results = vector_store.search(
            embedding=query_embedding,
            n_results=n_results,
        )

        return results


retriever = Retriever()