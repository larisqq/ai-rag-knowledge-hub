
from chromadb import PersistentClient

from app.core.config import settings


class VectorStore:
    """
    Provides an abstraction over ChromaDB operations.
    """

    def __init__(self):
        self.client = PersistentClient(
            path=settings.chroma_db_path
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )

    def add(
        self,
        ids,
        documents,
        embeddings,
        metadatas,
    ):
        """
        Store document chunks in ChromaDB.
        """

        self.collection.add(
            ids=ids,
            documents=documents,
            embeddings=embeddings,
            metadatas=metadatas,
        )

    def search(
        self,
        embedding,
        n_results,
    ):
        """
        Perform semantic similarity search.
        """

        return self.collection.query(
            query_embeddings=[embedding],
            n_results=n_results,
        )

    def get_all(self):
        """
        Return all indexed chunks and metadata.
        """

        return self.collection.get()

    def delete(self, ids):
        """
        Delete vectors by ids.
        """

        self.collection.delete(
            ids=ids
        )
    def delete_by_stored_filename(
        self,
        stored_filename: str,
    ):
        """
        Delete every chunk belonging to a stored PDF.
        """

        self.collection.delete(
            where={
                "stored_filename": stored_filename,
            }
        )


vector_store = VectorStore()