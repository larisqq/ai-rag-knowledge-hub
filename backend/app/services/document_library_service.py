from app.rag.vector_store import vector_store


class DocumentLibraryService:
    """
    Provides information about indexed documents.
    """

    @staticmethod
    def list_documents():
        """
        Return a list of indexed documents.
        """

        results = vector_store.get_all()

        documents = {}

        for metadata in results["metadatas"]:

            filename = metadata["filename"]

            if filename not in documents:

                documents[filename] = {
                    "filename": filename,
                    "chunks": metadata["total_chunks"],
                }

        return list(documents.values())


document_library_service = DocumentLibraryService()