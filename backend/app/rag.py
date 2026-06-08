import os
import chromadb
import ollama

DB_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../chroma_db"
    )
)

def ask_rag(question):

    client = chromadb.PersistentClient(path=DB_PATH)

    collection = client.get_collection("documents")

    results = collection.query(
        query_texts=[question],
        n_results=3
    )

    context = "\n\n".join(
        results["documents"][0]
    )

    prompt = f"""
Answer using ONLY the context below.

Context:
{context}

Question:
{question}
"""

    response = ollama.generate(
        model="qwen2.5:3b",
        prompt=prompt
    )

    return response["response"]
