from pathlib import Path

from pypdf import PdfReader


class PDFReader:

    @staticmethod
    def extract_text(pdf_path: str):

        reader = PdfReader(pdf_path)

        pages = []

        for index, page in enumerate(reader.pages):

            text = page.extract_text()

            if text:

                pages.append({
                    "page": index + 1,
                    "text": text
                })

        return pages


pdf_reader = PDFReader()