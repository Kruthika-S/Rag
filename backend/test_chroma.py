import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="test_collection"
)

collection.add(
    ids=["1"],
    documents=["RAG stands for Retrieval Augmented Generation"]
)

results = collection.query(
    query_texts=["What is RAG?"],
    n_results=1
)

print(results)

