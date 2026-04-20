from datetime import datetime
def check_balance(users, current_user):
    balance = users[current_user]["balance"]
    print(f"Your balance is: ₹{balance:.2f}")


def deposit(users, current_user):
    amount = float(input("Enter amount to deposit: "))

    if amount <= 0:
        print("Invalid amount")
        return

    users[current_user]["balance"] += amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    users[current_user]["history"].append(
        f"[{time}] Deposited ₹{amount}"
    )

    print("Deposit successful!")


def withdraw(users, current_user):
    amount = float(input("Enter amount to withdraw: "))

    if amount <= 0:
        print("Invalid amount")
        return

    if amount > users[current_user]["balance"]:
        print("Insufficient balance")
        return

    # Daily limit check
    if not check_daily_limit(users, current_user, amount):
        return

    users[current_user]["balance"] -= amount

    time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
    users[current_user]["history"].append(
        f"[{time}] Withdrew ₹{amount}"
    )

    users[current_user]["daily_withdraw"] += amount

    print("Withdraw successful!")


def show_history(users, current_user):
    print("\n--- Transaction History ---")
    history = users[current_user]["history"]

    if not history:
        print("No transactions yet.")
    else:
        for txn in history:
            print(txn)

def check_daily_limit(users, current_user, amount):
    from datetime import datetime

    user = users[current_user]

    if "daily_withdraw" not in user:
        user["daily_withdraw"] = 0

    if "last_withdraw_date" not in user:
        user["last_withdraw_date"] = ""

    today = datetime.now().strftime("%Y-%m-%d")

    # Reset daily limit if new day
    if user["last_withdraw_date"] != today:
        user["daily_withdraw"] = 0
        user["last_withdraw_date"] = today

    LIMIT = 10000  # ₹10,000/day

    if user["daily_withdraw"] + amount > LIMIT:
        print("Daily withdrawal limit exceeded (₹10,000)")
        return False

    return True