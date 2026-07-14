import ollama
from app.core.config import settings


class LLMService:
    """
    Handles communication with Ollama.
    """

    model = settings.ollama_model
    @classmethod
    def generate(cls, prompt: str) -> str:

        response = ollama.chat(
            model=cls.model,
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )

        return response["message"]["content"]


llm_service = LLMService()