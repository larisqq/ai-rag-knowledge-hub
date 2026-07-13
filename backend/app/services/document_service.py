from pathlib import Path
from uuid import uuid4

from fastapi import UploadFile


UPLOAD_FOLDER = Path("app/uploads/pdfs")


class DocumentService:

    @staticmethod
    async def save_pdf(file: UploadFile):

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


document_service = DocumentService()