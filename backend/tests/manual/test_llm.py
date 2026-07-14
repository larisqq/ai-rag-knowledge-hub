from app.rag.llm import llm_service

print("Asking Llama...")

answer = llm_service.generate(
    "What is FastAPI? Answer in one sentence."
)

print()
print(answer)