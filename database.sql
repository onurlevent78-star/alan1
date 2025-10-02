-- Rezervasyon Sistemi Database Schema

CREATE DATABASE IF NOT EXISTS rezervasyon_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
USE rezervasyon_db;

-- Kullanıcılar Tablosu
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) UNIQUE NOT NULL,
    password_hash VARCHAR(255) NOT NULL,
    role VARCHAR(20) NOT NULL DEFAULT 'user',
    permissions JSON,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

-- Rezervasyonlar Tablosu
CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name_surname VARCHAR(100) NOT NULL,
    center VARCHAR(100) NOT NULL,
    venue VARCHAR(50) NOT NULL DEFAULT 'Tiyatro Salonu',
    date DATE NOT NULL,
    time VARCHAR(20) NOT NULL,
    description TEXT,
    status ENUM('bekle', 'onay', 'iptal') DEFAULT 'bekle',
    created_by VARCHAR(50),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    INDEX idx_date_time (date, time),
    INDEX idx_center_venue (center, venue),
    INDEX idx_status (status)
);

-- Varsayılan Admin Kullanıcı (şifre: admin123)
INSERT INTO users (username, password_hash, role, permissions) VALUES 
('admin', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj0CyPm0KCHa', 'admin', 
 '["view_reservations", "edit_reservations", "view_availability", "manage_users"]');

-- Diğer Demo Kullanıcılar
INSERT INTO users (username, password_hash, role, permissions) VALUES 
('editor1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj0CyPm0KCHa', 'editor', '["edit_reservations"]'),
('viewer1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj0CyPm0KCHa', 'viewer', '["view_reservations"]'),
('scheduler1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj0CyPm0KCHa', 'scheduler', '["view_availability"]'),
('user1', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewdBPj0CyPm0KCHa', 'user', '[]');
