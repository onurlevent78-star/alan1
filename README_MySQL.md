# MySQL Rezervasyon Sistemi Kurulum Rehberi

## Gereksinimler

1. **MySQL Server** (8.0 veya üzeri)
2. **Python** (3.8 veya üzeri)
3. **pip** (Python paket yöneticisi)

## Kurulum Adımları

### 1. MySQL Server Kurulumu

- [MySQL Community Server](https://dev.mysql.com/downloads/mysql/) indirin ve kurun
- Root şifresini belirleyin
- MySQL Workbench (isteğe bağlı) kurun

### 2. Python Bağımlılıklarını Kurun

```bash
pip install -r requirements.txt
```

### 3. Veritabanı Yapılandırması

**app_mysql.py** dosyasındaki `DB_CONFIG` bölümünü düzenleyin:

```python
DB_CONFIG = {
    'host': 'localhost',
    'database': 'rezervasyon_sistemi',
    'user': 'root',
    'password': 'sizin_mysql_şifreniz',  # Buraya kendi şifrenizi yazın
    'port': 3306,
    'charset': 'utf8mb4'
}
```

### 4. Veritabanını Oluşturun (Opsiyonel)

Otomatik oluşturma yerine manuel olarak oluşturmak isterseniz:

```bash
mysql -u root -p < database_setup.sql
```

### 5. Uygulamayı Çalıştırın

```bash
python app_mysql.py
```

Uygulama ilk çalıştığında veritabanını ve tabloları otomatik oluşturacaktır.

## Özellikler

✅ **MySQL Veritabanı Desteği**
✅ **Otomatik Tablo Oluşturma**
✅ **UTF-8 Karakter Desteği**
✅ **İndekslenmiş Sorgular**
✅ **Hata Yönetimi**
✅ **Bağlantı Havuzu**

## Veritabanı Yapısı

### reservations Tablosu
- `id` - Otomatik artan birincil anahtar
- `name_surname` - Ad Soyad (VARCHAR 255)
- `center` - Kültür Merkezi (VARCHAR 255)
- `date` - Rezervasyon Tarihi (DATE)
- `time` - Rezervasyon Saati (VARCHAR 20)
- `description` - Açıklama (TEXT)
- `status` - Durum (ENUM: 'onay', 'bekle', 'iptal')
- `created_at` - Oluşturulma Tarihi (TIMESTAMP)
- `updated_at` - Güncellenme Tarihi (TIMESTAMP)

## Sorun Giderme

### Bağlantı Hatası
- MySQL servisinin çalıştığını kontrol edin
- Kullanıcı adı ve şifrenin doğru olduğunu kontrol edin
- Port numarasının doğru olduğunu kontrol edin

### Karakter Kodlama Sorunu
- MySQL'in utf8mb4 desteğini kontrol edin
- Veritabanı ve tabloların utf8mb4 ile oluşturulduğunu kontrol edin

### Performans İyileştirme
- `my.cnf` dosyasında innodb_buffer_pool_size ayarını yapın
- Yoğun kullanımda connection pooling kullanın
