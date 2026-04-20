MAX_ATTEMPTS = 3

def login(users):
    print("\n--- LOGIN ---")

    username = input("Enter username: ")

    if username not in users:
        print("User not found")
        return None

    attempts = 0

    while attempts < MAX_ATTEMPTS:
        pin = input("Enter PIN: ")

        if users[username]["pin"] == pin:
            print(f"Welcome, {username}!")
            return username
        else:
            attempts += 1
            print(f"Wrong PIN! Attempts left: {MAX_ATTEMPTS - attempts}")

    print("Too many wrong attempts. Account temporarily locked.")
    return None