from app.rag.vector_store import vector_store

print("Connecting to ChromaDB...")

collections = vector_store.client.list_collections()

print(collections)

print("Connection successful!")