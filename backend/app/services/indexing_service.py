from pathlib import Path
from uuid import uuid4

from app.rag.loader import pdf_loader
from app.rag.chunker import text_chunker
from app.rag.embeddings import embedding_service
from app.rag.vector_store import vector_store


class IndexingService:
    """
    Handles document indexing into the vector database.
    """

    @staticmethod
    def index_document(
    pdf_path: str,
    original_filename: str
):

        pdf_path = str(pdf_path)

        print("Loading PDF...")

        text = pdf_loader.load(pdf_path)

        print(f"Characters: {len(text)}")

        print("Chunking document...")

        chunks = text_chunker.split(text)

        print(f"Chunks: {len(chunks)}")

        print("Generating embeddings...")

        embeddings = embedding_service.embed_documents(chunks)

        print(f"Embeddings: {len(embeddings)}")

        ids = [str(uuid4()) for _ in chunks]

        stored_filename = Path(pdf_path).name

        metadatas = []

        for index in range(len(chunks)):
            metadatas.append(
                {
                    "source": pdf_path,
                    "filename": original_filename,
                    "stored_filename": stored_filename,
                    "chunk_index": index,
                    "total_chunks": len(chunks),
                }
            )
            

        print("Saving to ChromaDB...")

        vector_store.add(
            ids=ids,
            documents=chunks,
            embeddings=embeddings,
            metadatas=metadatas,
        )

        print("Done!")

        return len(chunks)


indexing_service = IndexingService()