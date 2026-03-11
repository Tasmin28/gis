# SMART FIELD MONITORING SYSTEM - Configuration

import os
from datetime import timedelta

class Config:
    """Base configuration"""
    
    # Base directory
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    # Secret key for sessions
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'smart-field-monitoring-secret-key-2024'
    
    # Database
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(BASE_DIR, 'database.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_ECHO = False
    
    # Session configuration
    SESSION_TYPE = 'filesystem'
    SESSION_PERMANENT = False
    PERMANENT_SESSION_LIFETIME = timedelta(hours=2)
    
    # Upload configuration
    UPLOAD_FOLDER = os.path.join(BASE_DIR, 'static', 'uploads', 'reports')
    MAX_CONTENT_LENGTH = 16 * 1024 * 1024  # 16MB max file size
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}
    
    # Application settings
    PAGINATION_PER_PAGE = 20
    MAP_CENTER_LAT = -6.2088  # Jakarta coordinates
    MAP_CENTER_LNG = 106.8456
    MAP_DEFAULT_ZOOM = 12
    
    # Date formats
    DATE_FORMAT = '%Y-%m-%d'
    DATETIME_FORMAT = '%Y-%m-%d %H:%M:%S'
    DISPLAY_DATE_FORMAT = '%d %B %Y'
    DISPLAY_DATETIME_FORMAT = '%d %B %Y, %H:%M'
    
    # Export settings
    EXPORT_FOLDER = os.path.join(BASE_DIR, 'exports')
    
    # API settings
    API_PREFIX = '/api'
    API_RATE_LIMIT = '100 per hour'
    
    # Logging
    LOG_FILE = os.path.join(BASE_DIR, 'app.log')
    LOG_LEVEL = 'INFO'
    
    # Pagination
    ITEMS_PER_PAGE = 10


class DevelopmentConfig(Config):
    """Development configuration"""
    DEBUG = True


class ProductionConfig(Config):
    """Production configuration"""
    DEBUG = False


# Default configuration
config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}

