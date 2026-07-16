from pathlib import Path
from uuid import uuid4

from fastapi import HTTPException, UploadFile

from app.core.config import settings
from app.rag.vector_store import vector_store


UPLOAD_FOLDER = Path(settings.upload_folder)


class DocumentService:
    """
    Handles document uploads and coordinates the indexing workflow.
    """

    @staticmethod
    async def save_pdf(file: UploadFile):
        """
        Save an uploaded PDF using a unique internal filename.
        """

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        original_filename = file.filename

        if not original_filename:
            raise HTTPException(
                status_code=400,
                detail="The uploaded file must have a filename.",
            )

        extension = Path(original_filename).suffix.lower()
        stored_filename = f"{uuid4()}{extension}"
        destination = UPLOAD_FOLDER / stored_filename

        content = await file.read()
        destination.write_bytes(content)

        return {
            "original_filename": original_filename,
            "stored_filename": stored_filename,
            "size": len(content),
            "path": str(destination),
        }

    @staticmethod
    async def upload(file: UploadFile):
        """
        Save and index an uploaded document.
        """

        from app.services.indexing_service import indexing_service

        document = await DocumentService.save_pdf(file)

        try:
            indexed_chunks = indexing_service.index_document(
                pdf_path=document["path"],
                original_filename=document["original_filename"],
            )
        except Exception:
            Path(document["path"]).unlink(missing_ok=True)
            raise

        document["indexed_chunks"] = indexed_chunks

        return document

    @staticmethod
    def delete(stored_filename: str):
        """
        Delete a document from disk and ChromaDB.
        """

        pdf_path = UPLOAD_FOLDER / stored_filename

        if not pdf_path.exists():
            raise HTTPException(
                status_code=404,
                detail="Document not found.",
            )

        vector_store.delete_by_stored_filename(stored_filename)

        pdf_path.unlink()

        return {
            "message": "Document deleted successfully.",
            "stored_filename": stored_filename,
        }


document_service = DocumentService()