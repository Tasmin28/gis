import os
import shutil

# Fix the nested folder structure
reports_reports = 'static/uploads/reports/reports'
reports_dir = 'static/uploads/reports'

# Move files from nested folder to main reports folder
if os.path.exists(reports_reports):
    for f in os.listdir(reports_reports):
        src = os.path.join(reports_reports, f)
        dst = os.path.join(reports_dir, f)
        if os.path.isfile(src):
            shutil.move(src, dst)
            print(f'Moved: {f}')

# Remove empty nested folder
if os.path.exists(reports_reports):
    try:
        os.rmdir(reports_reports)
        print('Removed nested folder')
    except:
        pass

print('Done fixing folder structure')
