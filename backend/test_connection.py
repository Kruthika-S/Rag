import psycopg2

conn = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    host="/tmp"
)

cur = conn.cursor()

cur.execute("SELECT version();")

print(cur.fetchone())

cur.close()
conn.close()

print("Connected Successfully!")

