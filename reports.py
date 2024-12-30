import sqlite3
def generate_monthly_report(user_id):
    month = input("Enter the month (MM): ")
    year = input("Enter the year (YYYY): ")
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT type, SUM(amount) FROM transactions 
                      WHERE user_id = ? AND strftime('%m', date) = ? AND strftime('%Y', date) = ? 
                      GROUP BY type''', (user_id, month, year))
    report = cursor.fetchall()
    income = sum(amount for txn_type, amount in report if txn_type == 'income')
    expenses = sum(amount for txn_type, amount in report if txn_type == 'expense')
    savings = income - expenses
    print(f"\nMonthly Report for {month}/{year}:")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Savings: {savings}")
    conn.close()

def generate_yearly_report(user_id):
    year = input("Enter the year (YYYY): ")
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT type, SUM(amount) FROM transactions 
                      WHERE user_id = ? AND strftime('%Y', date) = ? 
                      GROUP BY type''', (user_id, year))
    report = cursor.fetchall()
    income = sum(amount for txn_type, amount in report if txn_type == 'income')
    expenses = sum(amount for txn_type, amount in report if txn_type == 'expense')
    savings = income - expenses
    print(f"\nYearly Report for {year}:")
    print(f"Total Income: {income}")
    print(f"Total Expenses: {expenses}")
    print(f"Savings: {savings}")
    conn.close()