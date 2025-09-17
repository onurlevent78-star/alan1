from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Rezervasyonlar burada tutuluyor
reservations = []

@app.route('/', methods=['GET', 'POST'])
def rezervasyon():
    error = None
    if request.method == 'POST':
        yeni_merkez = request.form['kultur_merkezi']
        yeni_tarih = request.form['tarih']
        yeni_saat = request.form['saat']
        yeni_saat_dt = datetime.strptime(yeni_saat, "%H:%M")
        # Aynı kültür merkezi ve tarih için saat aralığı kontrolü (en az 1 saat aralıklı olmalı)
        for r in reservations:
            if r['kultur_merkezi'] == yeni_merkez and r['tarih'] == yeni_tarih:
                mevcut_saat_dt = datetime.strptime(r['saat'], "%H:%M")
                saat_fark = abs((yeni_saat_dt - mevcut_saat_dt).total_seconds()) / 3600
                if saat_fark < 1:
                    error = "Bu kültür merkezi bu tarih ve saatte doludur, lütfen başka saat seçiniz (en az 1 saat aralıklı olmalı)."
                    break
        if not error:
            rezervasyon = {
                'ad_soyad': request.form['ad_soyad'],
                'kultur_merkezi': yeni_merkez,
                'tarih': yeni_tarih,
                'saat': yeni_saat,
                'aciklama': request.form['aciklama']
            }
            reservations.append(rezervasyon)
            return redirect(url_for('rezervasyon'))
    # index.html arayüzü ile rezervasyonlar ve hata mesajı gönderiliyor
    return render_template('index.html', reservations=reservations, error=error)

if __name__ == '__main__':
    app.run(debug=True)