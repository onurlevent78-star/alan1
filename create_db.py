import sqlite3

conn = sqlite3.connect('rezervasyon.db')
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS reservations (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad_soyad TEXT NOT NULL,
    kultur_merkezi TEXT NOT NULL,
    tarih TEXT NOT NULL,
    saat TEXT NOT NULL,
    aciklama TEXT
)
""")

conn.commit()
conn.close()
