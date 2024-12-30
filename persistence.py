import os
def backup_data():
    backup_file = 'finance_app_backup.db'
    if os.path.exists('finance_app.db'):
        with open('finance_app.db', 'rb') as original, open(backup_file, 'wb') as backup:
            backup.write(original.read())
        print("Backup completed successfully.")
    else:
        print("No database file found to back up.")
def restore_data():
    backup_file = 'finance_app_backup.db'
    if os.path.exists(backup_file):
        with open(backup_file, 'rb') as backup, open('finance_app.db', 'wb') as original:
            original.write(backup.read())
        print("Data restored successfully.")
    else:
        print("No backup file found to restore.")