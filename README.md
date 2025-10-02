# 🎯 Rezervasyon Sistemi

Modern, güvenli ve kullanıcı dostu rezervasyon yönetim sistemi.

## ✨ Özellikler

- 🔐 **Kullanıcı Yetki Sistemi** - Admin, Editör, Görüntüleyici, Scheduler rolleri
- 📊 **Excel Export** - Filtrelenmiş verileri Excel olarak indirme
- 🏢 **Çoklu Merkez Desteği** - 4 farklı kültür merkezi
- 🎭 **Etkinlik Yeri Seçimi** - Tiyatro ve Seminer salonu
- ⏰ **Gerçek Zamanlı Saat Durumu** - Otomatik güncellenen müsaitlik
- 🔍 **Gelişmiş Filtreleme** - Merkez, tarih, durum bazlı filtreleme
- 📱 **Responsive Tasarım** - Mobil uyumlu arayüz
- 🔒 **Güvenlik** - Environment variables, CSRF koruması

## 🛠️ Teknolojiler

- **Backend:** Flask (Python)
- **Database:** MySQL 8.0+
- **Frontend:** Bootstrap 5, Font Awesome
- **Deploy:** Gunicorn, Nginx
- **Environment:** python-dotenv

## 🚀 Hızlı Başlangıç

### Geliştirme Ortamı

```bash
# Repository'yi klonla
git clone <repository-url>
cd rezervasyon_sistemi

# Bağımlılıkları kur
pip install -r requirements.txt

# Environment variables ayarla
cp .env.example .env
# .env dosyasını düzenle

# Uygulamayı çalıştır
python app.py
```

### Production Deploy

```bash
# Deploy script'ini çalıştır
sudo bash deploy.sh

# Veya manuel olarak:
sudo systemctl start rezervasyon
sudo systemctl enable rezervasyon
```

## 👥 Varsayılan Kullanıcılar

| Kullanıcı | Şifre | Rol | Yetkiler |
|-----------|-------|-----|----------|
| admin | admin123 | Admin | Tüm yetkiler |
| editor1 | editor123 | Editör | Rezervasyon düzenleme |
| viewer1 | viewer123 | Görüntüleyici | Sadece görüntüleme |
| scheduler1 | scheduler123 | Scheduler | Saat durumu |
| user1 | user123 | Kullanıcı | Rezervasyon oluşturma |

## 📁 Dosya Yapısı

```
rezervasyon_sistemi/
├── app.py                 # Ana uygulama
├── requirements.txt       # Python bağımlılıkları
├── .env                   # Environment variables
├── .env.production       # Production ayarları
├── gunicorn.conf.py      # Gunicorn yapılandırması
├── nginx.conf            # Nginx yapılandırması
├── rezervasyon.service   # Systemd service
├── deploy.sh             # Deploy script'i
└── templates/            # HTML şablonları
    ├── index.html
    ├── reservations.html
    ├── edit_reservation.html
    ├── availability.html
    ├── admin_users.html
    └── login.html
```

## 🔧 Yapılandırma

### Environment Variables

```env
# Database
DB_HOST=localhost
DB_DATABASE=rezervasyon_sistemi
DB_USER=root
DB_PASSWORD=your_password

# Flask
FLASK_SECRET_KEY=your-secret-key
FLASK_DEBUG=True
FLASK_HOST=0.0.0.0
FLASK_PORT=5001
```

### MySQL Kurulumu

```sql
CREATE DATABASE rezervasyon_sistemi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
CREATE USER 'rezervasyon_user'@'localhost' IDENTIFIED BY 'strong_password';
GRANT ALL PRIVILEGES ON rezervasyon_sistemi.* TO 'rezervasyon_user'@'localhost';
FLUSH PRIVILEGES;
```

## 📊 API Endpoints

- `GET /` - Ana sayfa (rezervasyon oluşturma)
- `GET /reservations` - Rezervasyon listesi
- `GET /availability` - Saat durumu
- `GET /export/excel` - Excel export
- `POST /reservation/update/<id>` - Rezervasyon güncelleme
- `GET /admin/users` - Kullanıcı yönetimi

## 🔒 Güvenlik

- Environment variables ile hassas bilgi yönetimi
- SQL injection koruması (parametreli sorgular)
- Session tabanlı kimlik doğrulama
- Rol bazlı erişim kontrolü
- HTTPS desteği (production)

## 📱 Mobil Uyumluluk

- Bootstrap 5 responsive grid
- Touch-friendly interface
- Mobil optimized forms
- Adaptive navigation

## 🚀 Production Notları

1. **SSL Sertifikası:** Let's Encrypt kullanın
2. **Database Backup:** Otomatik yedekleme kurun
3. **Monitoring:** Log dosyalarını izleyin
4. **Security:** Güvenlik güncellemelerini takip edin

## 📝 Changelog

### v1.0.0 (2025-01-01)
- ✅ İlk stable release
- ✅ MySQL entegrasyonu
- ✅ Excel export özelliği
- ✅ Etkinlik yeri seçimi
- ✅ Production deploy scripts

## 🤝 Katkıda Bulunma

1. Fork the project
2. Create feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 Lisans

Bu proje MIT lisansı altında lisanslanmıştır.

## 📞 İletişim

- **Geliştirici:** [Your Name]
- **Email:** [your.email@example.com]
- **GitHub:** [github.com/yourusername]
