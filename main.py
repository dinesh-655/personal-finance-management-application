from login import initialize_db, register_user, login_user
from transaction import add_transaction, update_transaction, delete_transaction, view_transactions
from reports import generate_monthly_report, generate_yearly_report
from budgeting import set_budget, check_budget
from persistence import backup_data, restore_data

def main():
    initialize_db()
    print("Welcome to the Personal Finance Management Application!")
    
    while True:
        print("\nMain Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            register_user()
        elif choice == '2':
            user_id = login_user()
            if user_id:
                manage_transactions(user_id)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

def manage_transactions(user_id):
    while True:
        print("\nTransaction Menu:")
        print("1. Add Transaction")
        print("2. Update Transaction")
        print("3. Delete Transaction")
        print("4. View Transactions")
        print("5. Generate Reports")
        print("6. Budgeting")
        print("7. Backup Data")
        print("8. Restore Data")
        print("9. Logout")
        choice = input("Choose an option: ")

        if choice == '1':
            add_transaction(user_id)
        elif choice == '2':
            update_transaction(user_id)
        elif choice == '3':
            delete_transaction(user_id)
        elif choice == '4':
            view_transactions(user_id)
        elif choice == '5':
            generate_reports(user_id)
        elif choice == '6':
            budgeting(user_id)
        elif choice == '7':
            backup_data()  # Backup data
        elif choice == '8':
            restore_data()  # Restore data from backup
        elif choice == '9':
            print("Logging out...")
            break
        else:
            print("Invalid option. Please try again.")

def generate_reports(user_id):
    print("\nReport Generation:")
    print("1. Generate Monthly Report")
    print("2. Generate Yearly Report")
    choice = input("Choose an option: ")

    if choice == '1':
        generate_monthly_report(user_id)
    elif choice == '2':
        generate_yearly_report(user_id)
    else:
        print("Invalid option. Please try again.")

def budgeting(user_id):
    print("\nBudgeting:")
    print("1. Set Budget")
    print("2. Check Budget")
    choice = input("Choose an option: ")
    if choice == '1':
        set_budget(user_id)  
    elif choice == '2':
        check_budget(user_id)   
    else:
        print("Invalid option. Please try again.")

if __name__ == '__main__':
    main()
