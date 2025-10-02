#!/bin/bash
# VPS Deploy Script for Rezervasyon Sistemi

echo "🚀 Rezervasyon Sistemi Deploy Script"
echo "======================================"

# Configuration
APP_DIR="/var/www/rezervasyon_sistemi"
SERVICE_NAME="rezervasyon"
USER="www-data"

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Functions
print_status() {
    echo -e "${GREEN}[INFO]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    print_error "Please run as root (use sudo)"
    exit 1
fi

# Update system
print_status "Updating system packages..."
apt update && apt upgrade -y

# Install required packages
print_status "Installing required packages..."
apt install -y python3 python3-pip python3-venv nginx mysql-server

# Create application directory
print_status "Creating application directory..."
mkdir -p $APP_DIR
mkdir -p $APP_DIR/logs
chown -R $USER:$USER $APP_DIR

# Copy application files
print_status "Copying application files..."
cp -r ./* $APP_DIR/
chown -R $USER:$USER $APP_DIR

# Create virtual environment
print_status "Creating Python virtual environment..."
sudo -u $USER python3 -m venv $APP_DIR/venv
sudo -u $USER $APP_DIR/venv/bin/pip install -r $APP_DIR/requirements.txt

# Copy production environment file
print_status "Setting up production environment..."
cp $APP_DIR/.env.production $APP_DIR/.env
chown $USER:$USER $APP_DIR/.env

# Setup MySQL
print_status "Setting up MySQL database..."
mysql -e "CREATE DATABASE IF NOT EXISTS rezervasyon_sistemi_prod CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;"
mysql -e "CREATE USER IF NOT EXISTS 'rezervasyon_user'@'localhost' IDENTIFIED BY 'super-secure-password-change-this';"
mysql -e "GRANT ALL PRIVILEGES ON rezervasyon_sistemi_prod.* TO 'rezervasyon_user'@'localhost';"
mysql -e "FLUSH PRIVILEGES;"

# Setup systemd service
print_status "Setting up systemd service..."
cp $APP_DIR/rezervasyon.service /etc/systemd/system/
systemctl daemon-reload
systemctl enable $SERVICE_NAME
systemctl start $SERVICE_NAME

# Setup Nginx
print_status "Setting up Nginx..."
cp $APP_DIR/nginx.conf /etc/nginx/sites-available/rezervasyon_sistemi
ln -sf /etc/nginx/sites-available/rezervasyon_sistemi /etc/nginx/sites-enabled/
rm -f /etc/nginx/sites-enabled/default
nginx -t && systemctl reload nginx

# Create logs directory
mkdir -p $APP_DIR/logs
chown -R $USER:$USER $APP_DIR/logs

print_status "✅ Deploy completed successfully!"
print_warning "⚠️  Don't forget to:"
print_warning "   1. Change database password in .env"
print_warning "   2. Change Flask secret key in .env"
print_warning "   3. Update domain name in nginx.conf"
print_warning "   4. Setup SSL certificate (Let's Encrypt)"

echo ""
echo "Service Status:"
systemctl status $SERVICE_NAME
echo ""
echo "Application should be running on: http://your-server-ip"
