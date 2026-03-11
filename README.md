# SMART FIELD MONITORING SYSTEM

A professional GIS-based field activity monitoring system built with Flask, Bootstrap 5, and Leaflet.js.

## Features

- **User Management**: Role-based access control (Admin, Supervisor, Petugas)
- **Field Reporting**: Submit activity reports with photos, GPS location, and descriptions
- **GIS Mapping**: Interactive map with color-coded markers by status
- **Staff Tracking**: Real-time location tracking of field officers
- **Dashboard Analytics**: Charts and statistics
- **Data Export**: Export to Excel and PDF
- **REST API**: Mobile app integration support
- **Modern UI**: Dark theme dashboard

## Technology Stack

- **Backend**: Python Flask
- **Database**: SQLite (can be upgraded to PostgreSQL)
- **Frontend**: Bootstrap 5, JavaScript, Leaflet.js
- **Authentication**: Flask-Login

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Steps

1. **Clone or extract the project**

2. **Create virtual environment (recommended)**
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate
   
   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Open browser**
   Navigate to: `http://127.0.0.1:5000`

## Default Login

| Role | Username | Password |
|------|----------|----------|
| Admin | admin | admin123 |
| Supervisor | supervisor | supervisor123 |
| Petugas | petugas1 | petugas123 |

## Project Structure

```
smart_field_monitoring/
├── app.py                 # Main application
├── config.py              # Configuration
├── requirements.txt       # Dependencies
├── README.md             # This file
│
├── templates/            # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── map.html
│   ├── reports.html
│   └── ...
│
├── static/               # Static files
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
│
├── models/               # Database models
│   ├── user.py
│   ├── report.py
│   └── location.py
│
├── routes/               # Application routes
│   ├── auth.py
│   ├── main.py
│   ├── reports.py
│   ├── map.py
│   ├── users.py
│   ├── api.py
│   └── export.py
│
└── utils/                # Utility functions
    ├── helpers.py
    ├── image_utils.py
    └── decorators.py
```

## API Endpoints

### Authentication
- `POST /api/auth/login` - User login
- `POST /api/auth/register` - User registration

### Reports
- `GET /api/reports` - Get all reports
- `POST /api/reports` - Create new report
- `GET /api/reports/<id>` - Get single report
- `PUT /api/reports/<id>` - Update report
- `DELETE /api/reports/<id>` - Delete report

### Users
- `GET /api/users` - Get all users
- `GET /api/users/<id>` - Get single user

### Location
- `POST /api/location` - Update user location
- `GET /api/location/<user_id>` - Get user location

### Statistics
- `GET /api/stats` - Get dashboard statistics

## Configuration

Edit `config.py` to customize:
- Database URI
- Upload folder
- Map center coordinates
- Session settings
- Secret key

## Screenshots

The application features:
- Modern dark-themed dashboard
- Interactive GIS map with markers
- User management interface
- Report submission form
- Analytics charts

## License

MIT License

## Support

For issues or questions, please create an issue in the project repository.

