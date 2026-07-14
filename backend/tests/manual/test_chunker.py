from pathlib import Path

from app.rag.loader import pdf_loader
from app.rag.chunker import text_chunker

pdf = next(Path("app/uploads/pdfs").glob("*.pdf"))

text = pdf_loader.load(pdf)

chunks = text_chunker.split(text)

print(f"Total chunks: {len(chunks)}")

print()

print("First chunk:", len(chunks[0]))

print("Second chunk:", len(chunks[1]))

print()

print("Last chunk:", len(chunks[-1]))
print()

print("First 100 chars of chunk 1")
print(chunks[0][:100])

print()

print("Last 100 chars of chunk 1")
print(chunks[0][-100:])

print()

print("First 100 chars of chunk 2")
print(chunks[1][:100])