from chromadb import PersistentClient


class VectorStore:

    def __init__(self):

        self.client = PersistentClient(
            path="chroma_db"
        )

        self.collection = self.client.get_or_create_collection(
            name="documents"
        )


vector_store = VectorStore()