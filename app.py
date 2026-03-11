"""
SMART FIELD MONITORING SYSTEM
Main Flask Application
"""

import os
from datetime import datetime
from flask import Flask, render_template
from flask_login import LoginManager

# Import db and models from models package
from models import db
from models.user import User
from models.report import Report
from models.location import LocationTracking

# Initialize login manager
login_manager = LoginManager()

def create_app():
    """Application Factory"""
    
    # Create Flask app
    app = Flask(
        __name__,
        template_folder='templates',
        static_folder='static'
    )
    
    # Load configuration
    app.config.from_object('config.Config')
    
    # Ensure upload folder exists
    os.makedirs(app.config.get('UPLOAD_FOLDER', 'static/uploads/reports'), exist_ok=True)
    os.makedirs(app.config.get('EXPORT_FOLDER', 'exports'), exist_ok=True)
    
    # Initialize extensions
    db.init_app(app)
    login_manager.init_app(app)
    login_manager.login_view = 'auth.login'
    login_manager.login_message = 'Please login to access this page.'
    login_manager.login_message_category = 'info'
    
    # Configure session
    app.secret_key = app.config.get('SECRET_KEY', 'smart-field-secret-key')
    
    # Register Jinja2 filters
    @app.template_filter('datetime')
    def datetime_filter(value, format='%d %B %Y, %H:%M'):
        if value:
            return value.strftime(format)
        return ''
    
    @app.template_filter('date')
    def date_filter(value, format='%d %B %Y'):
        if value:
            return value.strftime(format)
        return ''
    
    @app.template_filter('normalize_path')
    def normalize_path(value):
        """Normalize file path for web (replace backslashes with forward slashes)"""
        if value:
            return value.replace('\\', '/')
        return value
    
    # Register blueprints
    from routes.auth import auth_bp
    from routes.main import main_bp
    from routes.reports import reports_bp
    from routes.map import map_bp
    from routes.users import users_bp
    from routes.api import api_bp
    from routes.export import export_bp
    
    app.register_blueprint(auth_bp)
    app.register_blueprint(main_bp)
    app.register_blueprint(reports_bp)
    app.register_blueprint(map_bp)
    app.register_blueprint(users_bp)
    app.register_blueprint(api_bp)
    app.register_blueprint(export_bp)
    
    # User loader callback
    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))
    
    # Error handlers
    @app.errorhandler(404)
    def not_found_error(error):
        return {'error': 404, 'message': 'Page not found'}, 404
    
    @app.errorhandler(500)
    def internal_error(error):
        db.session.rollback()
        return {'error': 500, 'message': 'Internal server error'}, 500
    
    # Context processors
    @app.context_processor
    def inject_now():
        return {'now': datetime.utcnow()}
    
    @app.context_processor
    def inject_config():
        from flask import current_app
        return {
            'config': current_app.config,
            'version': '1.0.0'
        }
    
    @app.context_processor
    def inject_notifications():
        """Inject notification variables for all templates"""
        from flask_login import current_user
        if current_user.is_authenticated:
            return {
                'unread_notifications': 0,
                'recent_notifications': []
            }
        return {
            'unread_notifications': 0,
            'recent_notifications': []
        }
    
    # Create database tables
    with app.app_context():
        db.create_all()
        
        # Create default admin user if not exists
        create_default_admin(app)
        
        # Add some dummy data
        add_dummy_data(app)
    
    return app


def create_default_admin(app):
    """Create default admin user if not exists"""
    
    admin = User.query.filter_by(username='admin').first()
    
    if not admin:
        admin = User(
            username='admin',
            email='admin@smartfield.com',
            full_name='System Administrator',
            role='admin',
            phone='+6281234567890',
            department='IT',
            is_active=True
        )
        admin.set_password('admin123')
        
        db.session.add(admin)
        db.session.commit()
        
        print('Default admin user created!')
        print('Username: admin')
        print('Password: admin123')


def add_dummy_data(app):
    """Add dummy data for demonstration"""
    from datetime import timedelta
    import random
    
    # Check if we already have data
    if User.query.count() > 1:
        return
    
    # Create supervisor
    supervisor = User(
        username='supervisor',
        email='supervisor@smartfield.com',
        full_name='Budi Supervisor',
        role='supervisor',
        phone='+6281234567891',
        department='Operations',
        is_active=True
    )
    supervisor.set_password('supervisor123')
    db.session.add(supervisor)
    
    # Create petugas
    petugas1 = User(
        username='petugas1',
        email='petugas1@smartfield.com',
        full_name='Ahmad Petugas',
        role='petugas',
        phone='+6281234567892',
        department='Field Team',
        is_active=True
    )
    petugas1.set_password('petugas123')
    db.session.add(petugas1)
    
    petugas2 = User(
        username='petugas2',
        email='petugas2@smartfield.com',
        full_name='Siti Petugas',
        role='petugas',
        phone='+6281234567893',
        department='Field Team',
        is_active=True
    )
    petugas2.set_password('petugas123')
    db.session.add(petugas2)
    
    db.session.commit()
    
    # Create sample reports
    activities = [
        ('Inspection PJU Jalan Utama', 'Melakukan inspeksi lampu PJU di sepanjang jalan utama. Beberapa lampu perlu perbaikan.'),
        ('Pembersihan Drainase', 'Membersihkan drainase di area perkantoran yang tersumbat.'),
        ('Perbaikan Kerusakan Jalan', 'Melakukan perbaikan jalan yang berlubang di depan supermarket.'),
        ('Pengecatan Marka Jalan', 'Mengecat marka jalan yang sudah pudar di persimpangan.'),
        ('Pemangkasan Pohon', 'Memangkas pohon yang menghalangi jalan di kompleks perumahan.'),
        ('Inspeksi Tower', 'Melakukan inspeksi rutin tower telekomunikasi.'),
        ('Pemasangan Rambu', 'Memasang rambu baru di lokasi yang ditentukan.'),
        ('Survey Lokasi', 'Melakukan survey lokasi untuk proyek berikutnya.'),
    ]
    
    statuses = ['pending', 'progress', 'completed']
    priorities = ['low', 'normal', 'high', 'urgent']
    
    # Sample coordinates around Jakarta
    base_lat = -6.2088
    base_lng = 106.8456
    
    users = [petugas1, petugas2]
    
    for i, (activity_name, description) in enumerate(activities):
        # Random offset for location
        lat = base_lat + random.uniform(-0.02, 0.02)
        lng = base_lng + random.uniform(-0.02, 0.02)
        
        # Random date within last 30 days
        days_ago = random.randint(0, 30)
        report_date = datetime.utcnow() - timedelta(days=days_ago)
        
        report = Report(
            user_id=random.choice(users).id,
            activity_name=activity_name,
            description=description,
            latitude=lat,
            longitude=lng,
            location_accuracy=random.uniform(5, 20),
            status=random.choice(statuses),
            priority=random.choice(priorities),
            report_date=report_date,
            created_at=report_date
        )
        
        db.session.add(report)
    
    db.session.commit()
    
    print('Dummy data added successfully!')


# Create the application
app = create_app()


if __name__ == '__main__':
    # Run the application
    print('=' * 60)
    print('SMART FIELD MONITORING SYSTEM')
    print('=' * 60)
    print('Starting server...')
    print('Open your browser and visit: http://127.0.0.1:5000')
    print('')
    print('Default Login:')
    print('  Username: admin')
    print('  Password: admin123')
    print('=' * 60)
    
    app.run(debug=True, host='0.0.0.0', port=5000)
