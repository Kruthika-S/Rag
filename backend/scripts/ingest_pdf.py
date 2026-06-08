import sys
import os

sys.path.append(
    os.path.abspath(
        os.path.join(os.path.dirname(__file__), "..")
    )
)

import chromadb
from app.document_processor import extract_text, create_chunks

DB_PATH = os.path.abspath(
    os.path.join(
        os.path.dirname(__file__),
        "../../chroma_db"
    )
)

client = chromadb.PersistentClient(path=DB_PATH)

collection = client.get_or_create_collection(
    name="documents"
)

text = extract_text("backend/uploads/Cloud.pdf")

chunks = create_chunks(text)

for i, chunk in enumerate(chunks):
    collection.add(
        ids=[str(i)],
        documents=[chunk]
    )

print(f"Stored {len(chunks)} chunks")
