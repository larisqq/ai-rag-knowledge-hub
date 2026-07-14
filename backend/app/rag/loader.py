from pathlib import Path

from pypdf import PdfReader


class PDFLoader:
    """
    Reads PDF documents and extracts all text.
    """

    @staticmethod
    def load(file_path: str | Path) -> str:

        reader = PdfReader(file_path)

        pages = []

        for page in reader.pages:

            text = page.extract_text()

            if text:
                pages.append(text)

        return "\n".join(pages)


pdf_loader = PDFLoader()