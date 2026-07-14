from chromadb import PersistentClient

from app.core.config import settings


class VectorStore:
    """
    Handles all interactions with ChromaDB.
    """

    def __init__(self):

        self.client = PersistentClient(
            path=settings.chroma_db_path
        )

        self.collection = self.client.get_or_create_collection(
            name=settings.chroma_collection
        )


vector_store = VectorStore()