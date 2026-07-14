from app.services.chat_service import chat_service

question = "Who is the author of this book?"

print(f"\nQuestion:\n{question}\n")

answer = chat_service.ask(question)

print("=" * 80)
print("ANSWER")
print("=" * 80)
print(answer)