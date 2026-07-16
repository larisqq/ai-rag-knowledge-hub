from pydantic import BaseModel


class IndexedDocument(BaseModel):
    """
    Represents an indexed document returned by the API.
    """

    filename: str
    stored_filename: str
    chunks: int