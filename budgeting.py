import sqlite3
def set_budget(user_id):
    category = input("Enter the category for the budget (e.g., Food, Rent): ")
    amount = float(input("Enter the budget amount: "))

    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT OR REPLACE INTO budgets (user_id, category, amount) 
                      VALUES (?, ?, ?)''', (user_id, category, amount))
    conn.commit()
    conn.close()
    print("Budget set successfully!")

def check_budget(user_id):
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT b.category, b.amount, IFNULL(SUM(t.amount), 0) FROM budgets b 
                      LEFT JOIN transactions t 
                      ON b.user_id = t.user_id AND b.category = t.category AND t.type = 'expense'
                      WHERE b.user_id = ?
                      GROUP BY b.category''', (user_id,))
    budgets = cursor.fetchall()

    for category, budget_amount, spent in budgets:
        print(f"Category: {category}")
        print(f"Budget: {budget_amount}, Spent: {spent}")
        if spent > budget_amount:
            print("Warning: Budget exceeded for this category!")
    conn.close()