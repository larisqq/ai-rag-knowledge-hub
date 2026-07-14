from app.rag.embeddings import embedding_service
from app.rag.vector_store import vector_store


class Retriever:
    """
    Retrieves the most relevant chunks from ChromaDB.
    """

    @staticmethod
    def search(query: str, n_results: int = 4):

        print("Generating query embedding...")

        query_embedding = embedding_service.embed_query(query)

        print("Searching ChromaDB...")

        results = vector_store.collection.query(
            query_embeddings=[query_embedding],
            n_results=n_results,
        )

        return results


retriever = Retriever()