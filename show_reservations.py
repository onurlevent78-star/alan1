import os
import psycopg2

db_url = os.environ.get(
    'DATABASE_URL',
    'postgresql://rezervasyon_db_user:6PtiKFiQByOx1K913riicz74747rDNat@dpg-d35rcdnfte5s7396bgcg-a:5432/rezervasyon_db'
)
conn = psycopg2.connect(db_url, sslmode='require')
cur = conn.cursor()
cur.execute("SELECT * FROM reservations")
rows = cur.fetchall()
for row in rows:
    print(row)
cur.close()
conn.close()
