from backend.app.rag import ask_rag
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import psycopg2

app = FastAPI()

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

    cur.execute("SELECT COUNT(*) FROM employee")

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
