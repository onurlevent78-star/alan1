from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

reservations = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        ad_soyad = request.form.get('ad_soyad', '')
        merkez = request.form.get('merkez', '')
        tarih = request.form.get('tarih', '')
        saat = request.form.get('saat', '')
        aciklama = request.form.get('aciklama', '')

        # İzin verilen merkezler (küçük harf ve "kültür merkezi" eki)
        allowed_centers = ['sefaköy kültür merkezi', 'cennet kültür merkezi', 'atakent kültür merkezi']

        # Geçerli merkez değilse kayıt yapılmasın
        if merkez not in allowed_centers:
            return redirect(url_for('index'))

        reservation = {
            'ad_soyad': ad_soyad,
            'merkez': merkez,
            'tarih': tarih,
            'saat': saat,
            'aciklama': aciklama
        }

        reservations.append(reservation)
        return redirect(url_for('index'))

    return render_template('index.html', reservations=reservations)

if __name__ == '__main__':
    app.run(debug=True)