# Personal Finance Management Application

This is a personal finance management application that allows users to register, log in, manage transactions, set and check budgets, generate monthly and yearly reports, and perform backup/restore operations on the database.

## Features

- **User Management**: Register new users and log in with existing credentials.
- **Transaction Management**: Add, update, delete, and view financial transactions.
- **Budget Management**: Set and check budgets for various categories.
- **Report Generation**: Generate monthly and yearly financial reports.
- **Backup and Restore**: Backup the database and restore data from backup.

## Technologies Used

- **SQLite**: Database for storing user data, transactions, budgets, etc.
- **Python**: Backend logic for the application.
- **SQL**: For interacting with the SQLite database.

## Requirements

- Python 3.x
- `sqlite3` module (standard in Python)

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dinesh-655/personal-finance-management-application.git
    cd personal-finance-management-application
    ```

2. Install required dependencies (if any):
    ```bash
    pip install -r requirements.txt
    ```

    Note: There are no external dependencies in this project as it uses only Python's built-in modules (`sqlite3`).

3. Initialize the database:
    The database is initialized automatically when the app runs for the first time. However, you can manually initialize it by running:

    ```bash
    python main.py
    ```

## Usage

To run the application, execute the following command:

```bash
python main.py
```

## Testing

To test the application, execute the following command:

```bash
python testing.py
```
