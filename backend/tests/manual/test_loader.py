from pathlib import Path

from app.rag.loader import pdf_loader

pdf_folder = Path("app/uploads/pdfs")

pdf_file = next(pdf_folder.glob("*.pdf"))

print(f"Loading: {pdf_file.name}")

text = pdf_loader.load(pdf_file)

print("=" * 60)
print(text[:1500])
print("=" * 60)
print(f"Characters: {len(text)}")