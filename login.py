import sqlite3
from getpass import getpass
import bcrypt

# Database setup
def initialize_db():
    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS transactions (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        amount REAL NOT NULL,
        category TEXT NOT NULL,
        type TEXT NOT NULL, -- 'income' or 'expense'
        date TEXT NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    cursor.execute('''CREATE TABLE IF NOT EXISTS budgets (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        FOREIGN KEY(user_id) REFERENCES users(id)
    )''')
    conn.commit()
    conn.close()

def register_user():
    username = input("Enter a unique username: ")
    password = getpass("Enter a password: ")
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    try:
        conn = sqlite3.connect('finance_app.db')
        cursor = conn.cursor()
        cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
        conn.commit()
        print("Registration successful! You can now log in.")
    except sqlite3.IntegrityError:
        print("Username already exists. Please choose a different one.")
    finally:
        conn.close()

def login_user():
    username = input("Enter your username: ")
    password = getpass("Enter your password: ")

    conn = sqlite3.connect('finance_app.db')
    cursor = conn.cursor()
    cursor.execute('SELECT id, password FROM users WHERE username = ?', (username,))
    result = cursor.fetchone()

    if result and bcrypt.checkpw(password.encode('utf-8'), result[1]):
        print("Login successful! Welcome, ", username)
        return result[0]  # Return user ID
    else:
        print("Invalid username or password. Please try again.")
        return None