from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.chat_service import chat_service


router = APIRouter(
    prefix="/chat",
    tags=["Chat"],
)


@router.post(
    "",
    response_model=ChatResponse,
)
def chat(request: ChatRequest):
    """
    Answer a user question using the RAG pipeline.
    """

    response = chat_service.ask(
        request.question
    )

    return ChatResponse(**response)