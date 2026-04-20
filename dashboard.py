def show_dashboard(users, current_user):
    user = users[current_user]

    balance = user["balance"]
    history = user["history"]

    total_deposit = 0
    total_withdraw = 0

    for txn in history:
        if "Deposited" in txn:
            amount = float(txn.split("₹")[1])
            total_deposit += amount

        elif "Withdrew" in txn:
            amount = float(txn.split("₹")[1])
            total_withdraw += amount

    print("\n====== 📊 MINI BANK DASHBOARD ======")
    print(f"👤 User: {current_user}")
    print(f"💰 Current Balance: ₹{balance:.2f}")
    print(f"📥 Total Deposited: ₹{total_deposit:.2f}")
    print(f"📤 Total Withdrawn: ₹{total_withdraw:.2f}")
    print(f"🔢 Total Transactions: {len(history)}")

    print("\n--- 🕒 Recent Transactions ---")
    if not history:
        print("No transactions yet.")
    else:
        for txn in history[-5:]:  # last 5 transactions
            print(txn)

    print("====================================\n")