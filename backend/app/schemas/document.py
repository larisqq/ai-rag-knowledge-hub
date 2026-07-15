from pydantic import BaseModel


class IndexedDocument(BaseModel):
    filename: str
    chunks: int