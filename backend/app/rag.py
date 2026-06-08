import chromadb
import requests

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="documents"
)


def ask_rag(question):

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = "\n".join(results["documents"][0])

    prompt = f"""
Use the context below to answer.

Context:
{context}

Question:
{question}

Answer:
"""

    response = requests.post(
        "http://localhost:11434/api/generate",
        json={
            "model": "qwen2.5:3b",
            "prompt": prompt,
            "stream": False
        }
    )

    return response.json()["response"]

