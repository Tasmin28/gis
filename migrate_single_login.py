"""
Migration script to add single login columns to database
"""
import os
import sys

# Add the project directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app import app
from models import db

def migrate():
    """Add new columns for single session login"""
    with app.app_context():
        # Add session_token column (without UNIQUE constraint first)
        try:
            db.session.execute(db.text(
                "ALTER TABLE users ADD COLUMN session_token VARCHAR(64)"
            ))
            print("Added session_token column")
        except Exception as e:
            print(f"session_token column might already exist: {e}")
        
        # Add last_session_ip column
        try:
            db.session.execute(db.text(
                "ALTER TABLE users ADD COLUMN last_session_ip VARCHAR(45)"
            ))
            print("Added last_session_ip column")
        except Exception as e:
            print(f"last_session_ip column might already exist: {e}")
        
        db.session.commit()
        
        # Now make session_token unique
        try:
            db.session.execute(db.text(
                "CREATE UNIQUE INDEX IF NOT EXISTS idx_session_token ON users(session_token)"
            ))
            print("Created unique index on session_token")
        except Exception as e:
            print(f"Index might already exist: {e}")
        
        db.session.commit()
        print("Migration completed successfully!")

if __name__ == '__main__':
    migrate()

