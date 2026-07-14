from app.rag.prompts import SYSTEM_PROMPT
from app.rag.retriever import retriever
from app.rag.llm import llm_service


class ChatService:
    """
    Handles the complete RAG pipeline.
    """

    @staticmethod
    def ask(question: str) -> str:

        print("Searching relevant chunks...")

        results = retriever.search(question)

        documents = results["documents"][0]

        print(f"Retrieved {len(documents)} chunks.")

        context = "\n\n".join(documents)

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question,
        )

        print("Sending prompt to LLM...")

        answer = llm_service.generate(prompt)

        return answer


chat_service = ChatService()