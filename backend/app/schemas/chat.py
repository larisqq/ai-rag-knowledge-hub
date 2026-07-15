from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    Represents a user question sent to the chat endpoint.
    """

    question: str


class Source(BaseModel):
    """
    Represents a document chunk used to generate the answer.
    """

    filename: str

    chunk_index: int


class ChatResponse(BaseModel):
    """
    Represents the response returned by the RAG pipeline.
    """

    answer: str

    sources: list[Source]