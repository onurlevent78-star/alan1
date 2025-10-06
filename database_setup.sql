-- MySQL Veritabanı Kurulum Scripti

-- Veritabanını oluştur
CREATE DATABASE IF NOT EXISTS rezervasyon_sistemi CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;

-- Veritabanını kullan
USE rezervasyon_sistemi;

-- Rezervasyonlar tablosunu oluştur
CREATE TABLE IF NOT EXISTS reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_surname VARCHAR(255) NOT NULL COMMENT 'Ad Soyad',
    center VARCHAR(255) NOT NULL COMMENT 'Kültür Merkezi',
    date DATE NOT NULL COMMENT 'Rezervasyon Tarihi',
    time VARCHAR(20) NOT NULL COMMENT 'Rezervasyon Saati',
    description TEXT COMMENT 'Açıklama',
    status ENUM('onay', 'bekle', 'iptal') DEFAULT 'bekle' COMMENT 'Rezervasyon Durumu',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP COMMENT 'Oluşturulma Tarihi',
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP COMMENT 'Güncellenme Tarihi',
    
    -- İndeksler
    INDEX idx_center_date_time (center, date, time),
    INDEX idx_status (status),
    INDEX idx_date (date),
    INDEX idx_created_at (created_at)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_unicode_ci COMMENT='Rezervasyon Kayıtları';

-- Örnek veriler (isteğe bağlı)
-- INSERT INTO reservations (name_surname, center, date, time, description, status) VALUES
-- ('Ahmet Yılmaz', 'Sefaköy Kültür Merkezi', '2025-01-15', '09:00-10:00', 'Test rezervasyonu', 'onay'),
-- ('Ayşe Demir', 'Cennet Kültür Merkezi', '2025-01-15', '10:00-11:00', 'Etkinlik planlaması', 'bekle');
