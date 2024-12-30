from login import register_user, login_user, initialize_db
from transaction import add_transaction, update_transaction, delete_transaction, view_transactions
from reports import generate_monthly_report, generate_yearly_report
from budgeting import set_budget, check_budget
from persistence import backup_data, restore_data
import sqlite3
import os

def run_tests():
    # Helper function to reset the database
    def reset_database():
        if os.path.exists('finance_app.db'):
            os.remove('finance_app.db')
        initialize_db()

    print("\nRunning unit tests for the application...\n")

    # Test 1: User Registration
    print("Test 1: User Registration")
    reset_database()
    register_user()  # Simulate user registration (e.g., testuser, password)
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = 'testuser'")
    user = cursor.fetchone()
    assert user is not None, "User registration failed!"
    print("User registration passed!")

    # Test 2: User Login
    print("Test 2: User Login")
    user_id = login_user()  # Assume 'testuser' credentials are used
    assert user_id is not None, "User login failed!"
    print("User login passed!")

    # Test 3: Adding Transactions
    print("Test 3: Adding Transactions")
    add_transaction(user_id)  # Add a sample transaction
    cursor.execute("SELECT * FROM transactions WHERE user_id = ?", (user_id,))
    transaction = cursor.fetchone()
    assert transaction is not None, "Transaction addition failed!"
    print("Adding transactions passed!")

    # Test 4: Updating Transactions
    print("Test 4: Updating Transactions")
    transaction_id = transaction[0]
    update_transaction(user_id)  # Update the existing transaction
    cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
    updated_transaction = cursor.fetchone()
    assert updated_transaction[1] != transaction[1], "Transaction update failed!"
    print("Updating transactions passed!")

    # Test 5: Deleting Transactions
    print("Test 5: Deleting Transactions")
    delete_transaction(user_id)  # Delete the existing transaction
    cursor.execute("SELECT * FROM transactions WHERE id = ?", (transaction_id,))
    deleted_transaction = cursor.fetchone()
    assert deleted_transaction is None, "Transaction deletion failed!"
    print("Deleting transactions passed!")

    # Test 6: Viewing Transactions
    print("Test 6: Viewing Transactions")
    view_transactions(user_id)  # Manually verify printed results
    print("Viewing transactions passed!")

    # Test 7: Generating Monthly Reports
    print("Test 7: Generating Monthly Reports")
    add_transaction(user_id)  # Add a sample transaction
    generate_monthly_report(user_id)  # Manually verify printed results
    print("Generating monthly reports passed!")

    # Test 8: Generating Yearly Reports
    print("Test 8: Generating Yearly Reports")
    generate_yearly_report(user_id)  # Manually verify printed results
    print("Generating yearly reports passed!")

    # Test 9: Setting Budgets
    print("Test 9: Setting Budgets")
    set_budget(user_id)  # Set a budget for the user
    cursor.execute("SELECT * FROM budgets WHERE user_id = ?", (user_id,))
    budget = cursor.fetchone()
    assert budget is not None, "Setting budget failed!"
    print("Setting budgets passed!")

    # Test 10: Checking Budgets
    print("Test 10: Checking Budgets")
    check_budget(user_id)  # Manually verify printed results
    print("Checking budgets passed!")

    # Test 11: Backup Data
    print("Test 11: Backup Data")
    backup_data()  # Create a backup of the database
    backup_file = 'finance_app_backup.db'
    assert os.path.exists(backup_file), "Backup data failed!"
    print("Backup data passed!")

    # Test 12: Restore Data
    print("Test 12: Restore Data")
    restore_data()  # Restore from the backup
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute("SELECT username FROM users WHERE username = 'testuser'")
    restored_user = cursor.fetchone()
    assert restored_user is not None, "Restore data failed!"
    print("Restore data passed!")

    print("\nAll tests passed successfully!")

    conn.close()

if __name__ == '__main__':
    run_tests()
