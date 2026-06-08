import psycopg2

def get_connection():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        host="/tmp"
    )

    return conn
