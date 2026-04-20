from auth import login
from bank import check_balance, deposit, withdraw, show_history
from admin import admin_login, admin_menu
from dashboard import show_dashboard

users = {
    "aarush": {
        "pin": "2008",
        "balance": 5000,
        "history": [],
        "daily_withdraw": 0,
        "last_withdraw_date": ""
    },
    "renukaa": {
        "pin": "2007",
        "balance": 3000,
        "history": [],
        "daily_withdraw": 0,
        "last_withdraw_date": ""
    }
}


def user_menu(users, current_user):
    while True:
        show_dashboard(users, current_user)
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Transaction History")
        print("5. Logout")

        choice = input("Enter choice: ")

        if choice == "1":
            check_balance(users, current_user)

        elif choice == "2":
            deposit(users, current_user)

        elif choice == "3":
            withdraw(users, current_user)

        elif choice == "4":
            show_history(users, current_user)

        elif choice == "5":
            print("Logging out...")
            break

        else:
            print("Invalid choice")

# MAIN LOOP
while True:
    print("\n1. User Login")
    print("2. Admin Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        user = login(users)
        if user:
            user_menu(users, user)

    elif choice == "2":
        if admin_login():
            admin_menu(users)
        else:
            print("Invalid admin credentials")

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice")