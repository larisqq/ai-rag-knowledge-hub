from pathlib import Path

from app.services.indexing_service import indexing_service

pdf = next(Path("app/uploads/pdfs").glob("*.pdf"))

chunks = indexing_service.index_document(pdf)

print()

print(f"Indexed {chunks} chunks.")