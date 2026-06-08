from fastapi import FastAPI
import psycopg2

app = FastAPI()


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
