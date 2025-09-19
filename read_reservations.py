import os
import psycopg2

conn = psycopg2.connect(
    os.environ.get(
        'DATABASE_URL',
        'postgresql://rezervasyon_db_user:6PtiKFiQByOx1K913riicz74747rDNat@dpg-d35rcdnfte5s7396bgcg-a:5432/rezervasyon_db'
    ),
    sslmode='require'
)
cur = conn.cursor()

cur.execute("SELECT * FROM reservations;")
rows = cur.fetchall()
for row in rows:
    print(row)

cur.close()
conn.close()
