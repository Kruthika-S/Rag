from db import get_connection

conn = get_connection()

cur = conn.cursor()

cur.execute("SELECT COUNT(*) FROM employee")

count = cur.fetchone()

print("Employee Count:", count[0])

cur.close()
conn.close()
