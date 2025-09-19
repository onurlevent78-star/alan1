import os
import psycopg2
from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder="templates")

def get_db_connection():
    db_url = os.environ.get(
        'DATABASE_URL',
        'postgresql://rezervasyon_db_user:6PtiKFiQByOx1K913riicz74747rDNat@dpg-d35rcdnfte5s7396bgcg-a:5432/rezervasyon_db'
    )
    try:
        conn = psycopg2.connect(db_url, sslmode='require')
    except Exception as e:
        print("Localde bağlanılamıyor:", e)
        conn = None
    return conn

@app.route('/', methods=['GET', 'POST'])
def rezervasyon():
    error = None
    reservations = []
    # Rezervasyonları veritabanından çek
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT ad_soyad, kultur_merkezi, tarih, saat, aciklama FROM reservations ORDER BY tarih, saat")
    rows = cur.fetchall()
    for r in rows:
        reservations.append({
            'ad_soyad': r[0],
            'kultur_merkezi': r[1],
            'tarih': r[2],
            'saat': r[3],
            'aciklama': r[4]
        })
    if request.method == 'POST':
        yeni_merkez = request.form['kultur_merkezi']
        yeni_tarih = request.form['tarih']
        yeni_saat = request.form['saat']
        try:
            yeni_saat_dt = datetime.strptime(yeni_saat, "%H:%M")
        except ValueError:
            error = "Saat formatı hatalı!"
        if not error:
            # Aynı kültür merkezi ve tarih için saat aralığı kontrolü (en az 1 saat aralıklı olmalı)
            for r in reservations:
                if r['kultur_merkezi'] == yeni_merkez and r['tarih'] == yeni_tarih:
                    mevcut_saat_dt = datetime.strptime(r['saat'], "%H:%M")
                    saat_fark = abs((yeni_saat_dt - mevcut_saat_dt).total_seconds()) / 3600
                    if saat_fark < 1:
                        error = "Bu kültür merkezi bu tarih ve saatte doludur, lütfen başka saat seçiniz (en az 1 saat aralıklı olmalı)."
                        break
        if not error:
            cur.execute(
                "INSERT INTO reservations (ad_soyad, kultur_merkezi, tarih, saat, aciklama) VALUES (%s, %s, %s, %s, %s)",
                (request.form['ad_soyad'], yeni_merkez, yeni_tarih, yeni_saat, request.form['aciklama'])
            )
            conn.commit()
            cur.close()
            conn.close()
            return redirect(url_for('rezervasyon'))
    cur.close()
    conn.close()
    return render_template('index.html', reservations=reservations, error=error)

if __name__ == '__main__':
    app.run(debug=True)