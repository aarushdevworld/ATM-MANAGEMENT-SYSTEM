ADMIN_USERNAME = "admin"
ADMIN_PIN = "0000"


def admin_login():
    print("\n--- ADMIN LOGIN ---")
    username = input("Enter admin username: ")
    pin = input("Enter admin PIN: ")

    return username == ADMIN_USERNAME and pin == ADMIN_PIN


def admin_menu(users):
    while True:
        print("\n--- ADMIN PANEL ---")
        print("1. Add User")
        print("2. Remove User")
        print("3. View All Users")
        print("4. Exit Admin Panel")

        choice = input("Enter choice: ")

        if choice == "1":
            add_user(users)

        elif choice == "2":
            remove_user(users)

        elif choice == "3":
            view_users(users)

        elif choice == "4":
            break

        else:
            print("Invalid choice")


def add_user(users):
    username = input("Enter new username: ")
    if username in users:
        print("User already exists")
        return

    pin = input("Set PIN: ")
    users[username] = {
        "pin": pin,
        "balance": 0,
        "history": []
    }

    print("User added successfully")


def remove_user(users):
    username = input("Enter username to remove: ")

    if username in users:
        del users[username]
        print("User removed")
    else:
        print("User not found")


def view_users(users):
    print("\n--- ALL USERS ---")
    for user in users:
        print(f"{user} → Balance: ₹{users[user]['balance']}")