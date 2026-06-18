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

    client = chromadb.PersistentClient(
        path=DB_PATH
    )

    collection = client.get_collection(
        "documents"
    )

    results = collection.query(
        query_texts=[question],
        n_results=5
    )

    documents = results["documents"][0]

    print("\n========== CHUNKS USED ==========\n")

    for i, doc in enumerate(documents):

        source = "Unknown"

        if (
            "metadatas" in results
            and results["metadatas"]
            and results["metadatas"][0]
        ):
            metadata = results["metadatas"][0][i]

            if metadata and "source" in metadata:
                  source = metadata["source"]

        print(
             f"\n----- CHUNK {i+1} "
             f"({source}) -----\n"
        )

        print(doc[:500])

    print("\n===============================\n")
    context = "\n\n".join(documents)

    prompt = f"""
You are answering questions using multiple PDFs.


If information comes from multiple documents,
combine the information.

If the answer is not clearly available in the context,
say "Information not found in uploaded documents."

Context:
{context}

Question:
{question}
"""

    response = ollama.generate(
        model="qwen2.5:3b",
        prompt=prompt
    )

    pdf_names = []

    if (
        "metadatas" in results
        and results["metadatas"]
        and results["metadatas"][0]
    ):

        for metadata in results["metadatas"][0]:

            if (
                metadata
                and "source" in metadata
            ):
                pdf_names.append(
                    metadata["source"]
                )

    pdf_names = list(
        set(pdf_names)
    )

    return {
        "answer": response["response"],
        "sources": pdf_names
    }
