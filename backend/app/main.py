from backend.app.rag import ask_rag
from backend.app.document_processor import (
    extract_text,
    create_chunks
)

from fastapi import (
    FastAPI,
    UploadFile,
    File
)

from fastapi.middleware.cors import CORSMiddleware

import chromadb
import psycopg2
import shutil

app = FastAPI()

# Allow React frontend access

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def home():
    return {
        "message": "RAG Backend Running"
    }


@app.get("/employees/count")
def employee_count():

    conn = psycopg2.connect(
        host="/tmp",
        port="5432",
        database="postgres",
        user="postgres"
    )

    cur = conn.cursor()

    cur.execute(
        "SELECT COUNT(*) FROM employee"
    )

    count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return {
        "employee_count": count
    }


@app.post("/ask")
def ask(question: str):

    answer = ask_rag(question)

    return {
        "answer": answer
    }


@app.post("/upload")
async def upload_pdf(
    file: UploadFile = File(...)
):

    upload_path = (
        f"backend/uploads/{file.filename}"
    )

    with open(
        upload_path,
        "wb"
    ) as buffer:

        shutil.copyfileobj(
            file.file,
            buffer
        )

    text = extract_text(upload_path)

    chunks = create_chunks(text)

    client = chromadb.PersistentClient(
        path="./chroma_db"
    )

    collection = client.get_or_create_collection(
        name="documents"
    )

    for i, chunk in enumerate(chunks):

        collection.add(
            ids=[
                f"{file.filename}_{i}"
            ],
            documents=[chunk]
        )

    return {
        "message": f"{file.filename} uploaded successfully",
        "chunks": len(chunks)
    }
