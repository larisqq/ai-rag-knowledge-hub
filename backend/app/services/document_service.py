from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile

from app.core.config import settings


UPLOAD_FOLDER = Path(settings.upload_folder)


class DocumentService:
    """
    Handles document uploads and coordinates the indexing workflow.
    """

    @staticmethod
    async def save_pdf(file: UploadFile):
        """
        Save the uploaded PDF to the uploads directory.
        """

        UPLOAD_FOLDER.mkdir(parents=True, exist_ok=True)

        extension = Path(file.filename).suffix

        filename = f"{uuid4()}{extension}"

        destination = UPLOAD_FOLDER / filename

        content = await file.read()

        destination.write_bytes(content)

        return {
            "original_filename": file.filename,
            "stored_filename": filename,
            "size": len(content),
            "path": str(destination),
        }

    @staticmethod
    async def upload(file: UploadFile):
        """
        Save the uploaded document and index it into ChromaDB.
        """

        # Import here to avoid circular imports.
        from app.services.indexing_service import indexing_service

        # Save PDF.
        document = await DocumentService.save_pdf(file)

        # Index document.
        indexed_chunks = indexing_service.index_document(
            pdf_path=document["path"],
            original_filename=document["original_filename"]
        )

        # Include indexing information.
        document["indexed_chunks"] = indexed_chunks

        return document


document_service = DocumentService()