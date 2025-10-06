import mysql.connector
from mysql.connector import Error
import os
import json
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        self.connection = None
        self.connect()
    
    def connect(self):
        """MySQL veritabanına bağlan"""
        try:
            self.connection = mysql.connector.connect(
                host=os.getenv('DB_HOST', 'localhost'),
                port=int(os.getenv('DB_PORT', 3306)),
                database=os.getenv('DB_NAME', 'rezervasyon_db'),
                user=os.getenv('DB_USER', 'root'),
                password=os.getenv('DB_PASSWORD', ''),
                charset='utf8mb4',
                autocommit=True
            )
            print("✅ MySQL bağlantısı başarılı!")
        except Error as e:
            print(f"❌ MySQL bağlantı hatası: {e}")
            self.connection = None
    
    def execute_query(self, query, params=None):
        """SQL sorgusu çalıştır"""
        if not self.connection or not self.connection.is_connected():
            self.connect()
        
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params or ())
            
            if query.strip().upper().startswith('SELECT'):
                result = cursor.fetchall()
                cursor.close()
                return result
            else:
                self.connection.commit()
                result = cursor.lastrowid or cursor.rowcount
                cursor.close()
                return result
        except Error as e:
            print(f"❌ SQL Hatası: {e}")
            return None
    
    def close(self):
        """Bağlantıyı kapat"""
        if self.connection and self.connection.is_connected():
            self.connection.close()

# Global database instance
db = Database()

# Database helper functions
def get_users():
    """Tüm kullanıcıları getir"""
    query = "SELECT * FROM users"
    users_data = db.execute_query(query)
    
    if not users_data:
        return {}
    
    users = {}
    for user in users_data:
        users[user['username']] = {
            'password': user['password_hash'],
            'role': user['role'],
            'permissions': json.loads(user['permissions']) if user['permissions'] else []
        }
    return users

def get_reservations():
    """Tüm rezervasyonları getir"""
    query = """
    SELECT id, name_surname, center, venue, date, time, description, 
           status, created_by, created_at, updated_at
    FROM reservations 
    ORDER BY created_at DESC
    """
    result = db.execute_query(query)
    
    if not result:
        return []
    
    reservations = []
    for row in result:
        reservation = {
            'id': row['id'],
            'name_surname': row['name_surname'],
            'center': row['center'],
            'venue': row['venue'],
            'date': row['date'].strftime('%Y-%m-%d'),
            'time': row['time'],
            'description': row['description'],
            'status': row['status'],
            'created_by': row['created_by'],
            'created_at': row['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
            'updated_at': row['updated_at'].strftime('%Y-%m-%d %H:%M:%S') if row['updated_at'] else None
        }
        reservations.append(reservation)
    
    return reservations

def add_reservation(data):
    """Yeni rezervasyon ekle"""
    query = """
    INSERT INTO reservations (name_surname, center, venue, date, time, description, status, created_by)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    params = (
        data['name_surname'], data['center'], data['venue'],
        data['date'], data['time'], data['description'],
        data['status'], data['created_by']
    )
    return db.execute_query(query, params)

def update_reservation(reservation_id, data):
    """Rezervasyon güncelle"""
    query = """
    UPDATE reservations 
    SET name_surname=%s, center=%s, venue=%s, date=%s, time=%s, description=%s
    WHERE id=%s
    """
    params = (
        data['name_surname'], data['center'], data['venue'],
        data['date'], data['time'], data['description'], reservation_id
    )
    return db.execute_query(query, params)

def update_reservation_status(reservation_id, status):
    """Rezervasyon durumu güncelle"""
    query = "UPDATE reservations SET status=%s WHERE id=%s"
    return db.execute_query(query, (status, reservation_id))

def delete_reservation(reservation_id):
    """Rezervasyon sil"""
    query = "DELETE FROM reservations WHERE id=%s"
    return db.execute_query(query, (reservation_id,))

def get_reservation_by_id(reservation_id):
    """ID ile rezervasyon getir"""
    query = "SELECT * FROM reservations WHERE id=%s"
    result = db.execute_query(query, (reservation_id,))
    
    if not result:
        return None
    
    row = result[0]
    return {
        'id': row['id'],
        'name_surname': row['name_surname'],
        'center': row['center'],
        'venue': row['venue'],
        'date': row['date'].strftime('%Y-%m-%d'),
        'time': row['time'],
        'description': row['description'],
        'status': row['status'],
        'created_by': row['created_by'],
        'created_at': row['created_at'].strftime('%Y-%m-%d %H:%M:%S'),
        'updated_at': row['updated_at'].strftime('%Y-%m-%d %H:%M:%S') if row['updated_at'] else None
    }
