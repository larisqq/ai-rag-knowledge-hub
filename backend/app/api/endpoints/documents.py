#backend/app/api/endpoints/documents.py
from fastapi import APIRouter, File, UploadFile

from app.services.document_service import document_service
from app.utils.validators import validate_pdf
from app.services.document_library_service import (
    document_library_service,
)

from app.schemas.document import IndexedDocument

router = APIRouter(
    prefix="/documents",
    tags=["Documents"],
)


@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    """
    Upload a PDF document and index it for semantic search.
    """

    await validate_pdf(file)

    return await document_service.upload(file)

@router.get(
    "",
    response_model=list[IndexedDocument],
)
def list_documents():
    """
    Return all indexed documents.
    """

    return document_library_service.list_documents()