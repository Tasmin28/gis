# Database migration script to add is_online and last_online columns to users table
import sqlite3
import os

def migrate():
    db_path = os.path.join(os.path.dirname(__file__), 'database.db')
    
    if not os.path.exists(db_path):
        print("Database not found!")
        return
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()
    
    # Check if columns exist
    cursor.execute("PRAGMA table_info(users)")
    columns = [col[1] for col in cursor.fetchall()]
    
    # Add is_online column if not exists
    if 'is_online' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN is_online BOOLEAN DEFAULT 0")
        print("Added is_online column")
    
    # Add last_online column if not exists
    if 'last_online' not in columns:
        cursor.execute("ALTER TABLE users ADD COLUMN last_online TIMESTAMP")
        print("Added last_online column")
    
    conn.commit()
    conn.close()
    print("Migration completed successfully!")

if __name__ == '__main__':
    migrate()

