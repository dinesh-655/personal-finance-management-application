import sqlite3
from datetime import datetime

def add_transaction(user_id):
    amount = float(input("Enter the amount: "))
    category = input("Enter the category (e.g., Food, Rent, Salary): ")
    transaction_type = input("Enter the type (income/expense): ").lower()
    date = datetime.now().strftime("%Y-%m-%d")  # Get current date in YYYY-MM-DD format

    if transaction_type not in ('income', 'expense'):
        print("Invalid transaction type. Please enter 'income' or 'expense'.")
        return

    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO transactions (user_id, amount, category, type, date) 
                      VALUES (?, ?, ?, ?, ?)''', (user_id, amount, category, transaction_type, date))
    conn.commit()
    conn.close()
    print("Transaction added successfully!")

def update_transaction(user_id):
    transaction_id = int(input("Enter the transaction ID to update: "))
    amount = float(input("Enter the new amount: "))
    category = input("Enter the new category: ")
    transaction_type = input("Enter the new type (income/expense): ").lower()
    date = datetime.now().strftime("%Y-%m-%d")  # Automatically fetch the current date

    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE transactions 
                      SET amount = ?, category = ?, type = ?, date = ?
                      WHERE id = ? AND user_id = ?''', 
                   (amount, category, transaction_type, date, transaction_id, user_id))
    if cursor.rowcount == 0:
        print("No transaction found with the given ID for this user.")
    else:
        print("Transaction updated successfully!")
    conn.commit()
    conn.close()

def delete_transaction(user_id):
    transaction_id = int(input("Enter the transaction ID to delete: "))

    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('DELETE FROM transactions WHERE id = ? AND user_id = ?', (transaction_id, user_id))
    if cursor.rowcount == 0:
        print("No transaction found with the given ID for this user.")
    else:
        print("Transaction deleted successfully!")
    conn.commit()
    conn.close()

def view_transactions(user_id):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, amount, category, type, date FROM transactions WHERE user_id = ?', (user_id,))
    transactions = cursor.fetchall()

    if transactions:
        print("\nYour Transactions:")
        print("ID | Amount | Category | Type | Date")
        print("-" * 40)
        for txn in transactions:
            print(f"{txn[0]} | {txn[1]} | {txn[2]} | {txn[3]} | {txn[4]}")
    else:
        print("No transactions found.")
    conn.close()
