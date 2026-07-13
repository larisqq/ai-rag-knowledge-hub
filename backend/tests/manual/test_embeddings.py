print("TEST STARTED")

from app.rag.embeddings import embedding_service

print("IMPORT OK")

texts = [
    "Berlin is the capital of Germany.",
    "Python is a programming language."
]

print("GENERATING EMBEDDINGS...")

vectors = embedding_service.embed_documents(texts)

print("DONE")
print(vectors[0][:5])