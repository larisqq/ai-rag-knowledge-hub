from app.rag.retriever import retriever

question = "Who is the author of this book?"

results = retriever.search(question)

print()

documents = results["documents"][0]

for i, document in enumerate(documents, start=1):
    print("=" * 70)
    print(f"Result {i}")
    print("=" * 70)
    print(document[:500])
    print()