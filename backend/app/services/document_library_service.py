from app.rag.vector_store import vector_store


class DocumentLibraryService:
    """
    Provides information about indexed documents.
    """

    @staticmethod
    def list_documents():
        """
        Return a deduplicated list of indexed documents.
        """

        results = vector_store.get_all()

        documents = {}

        for metadata in results.get("metadatas", []):
            if not metadata:
                continue

            stored_filename = metadata.get("stored_filename")
            filename = metadata.get("filename")
            total_chunks = metadata.get("total_chunks", 0)

            if not stored_filename or not filename:
                continue

            if stored_filename not in documents:
                documents[stored_filename] = {
                    "filename": filename,
                    "stored_filename": stored_filename,
                    "chunks": total_chunks,
                }

        return list(documents.values())


document_library_service = DocumentLibraryService()