from app.rag.prompts import SYSTEM_PROMPT
from app.rag.retriever import retriever
from app.rag.llm import llm_service


class ChatService:
    """
    Handles the complete Retrieval-Augmented Generation (RAG) pipeline.
    """

    @staticmethod
    def ask(question: str):
        """
        Retrieve relevant document chunks and generate an answer using the LLM.
        """

        print("Searching relevant chunks...")

        results = retriever.search(question)

        documents = results["documents"][0]
        metadatas = results["metadatas"][0]

        print(f"Retrieved {len(documents)} chunks.")

        context = "\n\n".join(documents)

        prompt = SYSTEM_PROMPT.format(
            context=context,
            question=question,
        )

        print("Sending prompt to LLM...")

        answer = llm_service.generate(prompt)

        sources = []

        for metadata in metadatas:
            sources.append(
                {
                    "filename": metadata["filename"],
                    "chunk_index": metadata["chunk_index"],
                }
            )

        return {
            "answer": answer,
            "sources": sources,
        }


chat_service = ChatService()