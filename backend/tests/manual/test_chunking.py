from app.rag.pdf_reader import pdf_reader
from app.rag.chunker import chunker

pages = pdf_reader.extract_text(
    "app/uploads/pdfs/NUMELE_PDF.pdf"
)

chunks = chunker.split(pages)

print(f"Pages: {len(pages)}")
print(f"Chunks: {len(chunks)}")

print()

print(chunks[0]["content"][:1000])