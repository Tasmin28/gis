# SMART FIELD MONITORING SYSTEM - Specification

## 1. PROJECT OVERVIEW

**Project Name**: SMART FIELD MONITORING SYSTEM  
**Type**: Web-based GIS Field Monitoring Application  
**Core Functionality**: Real-time field activity monitoring with GPS-enabled reporting, interactive GIS mapping, and comprehensive user management  
**Target Users**: Field Officers (Petugas), Supervisors, Administrators

---

## 2. TECHNOLOGY STACK

### Backend
- **Framework**: Flask 2.3.x (Python)
- **Database**: SQLite with SQLAlchemy ORM
- **Authentication**: Flask-Login
- **Password Hashing**: Werkzeug security

### Frontend
- **Framework**: Bootstrap 5.3
- **Maps**: Leaflet.js 1.9.4 with OpenStreetMap
- **Charts**: Chart.js 4.x
- **Icons**: Bootstrap Icons
- **Date Handling**: Flatpickr

### Additional Libraries
- **Geolocation**: geopy
- **Image Processing**: Pillow (for metadata validation)
- **Excel Export**: openpyxl
- **PDF Export**: ReportLab
- **API**: Flask-RESTful

---

## 3. DATABASE SCHEMA

### Users Table
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | User ID |
| username | String(50) | Unique username |
| email | String(100) | User email |
| password_hash | String(256) | Hashed password |
| role | String(20) | admin/supervisor/petugas |
| full_name | String(100) | Full name |
| phone | String(20) | Phone number |
| is_active | Boolean | Account status |
| created_at | DateTime | Creation timestamp |
| last_login | DateTime | Last login time |

### Reports Table
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Report ID |
| user_id | Integer (FK) | Reporter ID |
| activity_name | String(200) | Activity name |
| description | Text | Activity description |
| photo_path | String(300) | Photo file path |
| latitude | Float | GPS latitude |
| longitude | Float | GPS longitude |
| photo_latitude | Float | Photo EXIF latitude |
| photo_longitude | Float | Photo EXIF longitude |
| photo_datetime | DateTime | Photo timestamp |
| status | String(20) | pending/progress/completed |
| report_date | DateTime | Report submission time |
| created_at | DateTime | Creation timestamp |

### Activity Logs Table
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Log ID |
| user_id | Integer (FK) | User ID |
| action | String(100) | Action description |
| ip_address | String(45) | IP address |
| created_at | DateTime | Action timestamp |

### Location Tracking Table
| Field | Type | Description |
|-------|------|-------------|
| id | Integer (PK) | Location ID |
| user_id | Integer (FK) | User ID |
| latitude | Float | Current latitude |
| longitude | Float | Current longitude |
| accuracy | Float | GPS accuracy |
| timestamp | DateTime | Location time |

---

## 4. UI/UX SPECIFICATION

### Color Palette
- **Primary**: #1a73e8 (Google Blue)
- **Secondary**: #5f6368 (Gray)
- **Success**: #34a853 (Green)
- **Warning**: #fbbc04 (Yellow)
- **Danger**: #ea4335 (Red)
- **Dark Background**: #1e1e2f
- **Card Background**: #27293d
- **Text Primary**: #ffffff
- **Text Secondary**: #9a9a9a

### Typography
- **Font Family**: 'Segoe UI', 'Poppins', sans-serif
- **Headings**: 600 weight
- **Body**: 400 weight
- **Font Sizes**:
  - H1: 2.5rem
  - H2: 2rem
  - H3: 1.5rem
  - Body: 1rem
  - Small: 0.875rem

### Layout
- **Sidebar**: Fixed left, 260px width, collapsible
- **Header**: Fixed top, 60px height
- **Content**: Fluid with 20px padding
- **Cards**: Rounded corners (12px), subtle shadows

### Map Markers
- **Completed**: Green (#34a853) marker
- **In Progress**: Yellow (#fbbc04) marker
- **Pending**: Red (#ea4335) marker
- **User Location**: Blue pulsing marker

---

## 5. FUNCTIONAL SPECIFICATIONS

### 5.1 Authentication System
- Login with username/password
- Role-based access control
- Session management
- Password reset capability
- Login activity logging

### 5.2 User Management (Admin Only)
- Create new users
- Edit user details
- Delete/deactivate users
- Reset passwords
- View user activity

### 5.3 Field Reporting
- Activity name input
- Description textarea
- Photo upload with:
  - File type validation (jpg, png, jpeg)
  - File size limit (10MB max)
  - EXIF GPS data extraction
  - Timestamp validation
- Automatic GPS location capture
- Date/time picker
- Status selection (pending/progress/completed)

### 5.4 GIS Map Monitoring
- Interactive Leaflet map
- Clustered markers for multiple reports
- Color-coded markers by status
- Popup with:
  - Activity photo thumbnail
  - Reporter name
  - Report timestamp
  - Activity description
  - Status badge
- Filter by date range
- Filter by status
- Filter by user

### 5.5 Staff Tracking
- Real-time location updates
- Movement path visualization
- Activity timeline
- Last seen status

### 5.6 Dashboard Analytics
- Today's report count
- Active staff count
- Status distribution chart
- Weekly activity chart
- Heatmap layer on map

### 5.7 Notifications
- Dashboard notification bell
- Unread notification badge
- Notification list
- Mark as read functionality

### 5.8 Data Export
- Export reports to Excel
- Export reports to PDF
- Date range filtering
- Custom column selection

### 5.9 REST API
- POST /api/auth/login
- POST /api/auth/register
- GET /api/reports
- POST /api/reports
- GET /api/reports/<id>
- GET /api/users
- POST /api/location
- GET /api/stats

---

## 6. SECURITY MEASURES

- CSRF protection
- Password hashing with salt
- Session timeout (30 minutes)
- Role-based route protection
- File type validation
- SQL injection prevention (SQLAlchemy)
- XSS prevention (Jinja2 auto-escaping)

---

## 7. FOLDER STRUCTURE

```
smart_field_monitoring/
├── app.py                    # Main application
├── config.py                 # Configuration
├── requirements.txt          # Dependencies
├── database.db              # SQLite database
├── instance/                # Instance folder
├── templates/               # HTML templates
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── map.html
│   ├── reports.html
│   ├── users.html
│   ├── report_form.html
│   ├── profile.html
│   ├── settings.html
│   ├── notifications.html
│   └── export.html
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   ├── main.js
│   │   ├── map.js
│   │   ├── charts.js
│   │   └── notifications.js
│   └── uploads/
│       └── reports/
├── models/
│   ├── __init__.py
│   ├── user.py
│   ├── report.py
│   └── location.py
├── routes/
│   ├── __init__.py
│   ├── auth.py
│   ├── main.py
│   ├── reports.py
│   ├── map.py
│   ├── users.py
│   ├── api.py
│   └── export.py
└── utils/
    ├── __init__.py
    ├── helpers.py
    ├── image_utils.py
    └── decorators.py
```

---

## 8. ACCEPTANCE CRITERIES

### Authentication
- [ ] User can login with valid credentials
- [ ] Invalid credentials show error message
- [ ] Different roles see different menus
- [ ] Logout clears session

### Reporting
- [ ] Form captures all required fields
- [ ] Photo validates for type and size
- [ ] GPS location auto-captures
- [ ] Report saves to database

### Map
- [ ] Map loads with OpenStreetMap tiles
- [ ] All reports show as markers
- [ ] Markers are color-coded by status
- [ ] Clicking marker shows popup

### Admin
- [ ] Can create new users
- [ ] Can edit existing users
- [ ] Can delete users
- [ ] Can view activity logs

### Export
- [ ] Excel download works
- [ ] PDF download works
- [ ] Date filtering works

