import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_collection("documents")

results = collection.query(
    query_texts=["What is EC2?"],
    n_results=3
)

print(results["documents"])
