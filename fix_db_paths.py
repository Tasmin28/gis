import sqlite3
import os

db_path = 'database.db'
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Get all reports with photo_path
cursor.execute("SELECT id, photo_path FROM reports WHERE photo_path IS NOT NULL")
reports = cursor.fetchall()

print("Current paths in database:")
for r in reports:
    print(f"  Report {r[0]}: {r[1]}")

# Fix the paths - remove the duplicate 'reports/' 
for report_id, photo_path in reports:
    if photo_path and 'reports/reports' in photo_path:
        new_path = photo_path.replace('reports/reports', 'reports')
        cursor.execute("UPDATE reports SET photo_path = ? WHERE id = ?", (new_path, report_id))
        print(f"Fixed report {report_id}: {photo_path} -> {new_path}")

conn.commit()
conn.close()
print("\nDatabase paths fixed!")
