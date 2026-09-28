# Single-cell Banking System (CLI using input)
print("Starting Banking System - respond to prompts below.\n")

bank_data = {}
transaction_history = {}

def create_account():
    username = input("Enter new username: ")
    if username in bank_data:
        print("Username exists.")
        return
    pwd = input("Enter password: ")
    bank_data[username] = {"password": pwd, "balance": 0}
    transaction_history[username] = []
    print("Account created.")

def login():
    username = input("Username: ")
    pwd = input("Password: ")
    if username in bank_data and bank_data[username]['password'] == pwd:
        print(f"Welcome {username}")
        return username
    else:
        print("Invalid credentials.")
        return None

def deposit(user):
    amt = float(input("Amount to deposit: "))
    bank_data[user]["balance"] += amt
    transaction_history[user].append(f"+ {amt}")
    print("Deposited.")

def withdraw(user):
    amt = float(input("Amount to withdraw: "))
    if amt > bank_data[user]["balance"]:
        print("Insufficient funds.")
    else:
        bank_data[user]["balance"] -= amt
        transaction_history[user].append(f"- {amt}")
        print("Withdrawn.")

def check_balance(user):
    print("Balance:", bank_data[user]["balance"])

def transfer(user):
    recv = input("Receiver username: ")
    if recv not in bank_data:
        print("Receiver not found.")
        return
    amt = float(input("Amount to transfer: "))
    if amt > bank_data[user]["balance"]:
        print("Insufficient funds.")
    else:
        bank_data[user]["balance"] -= amt
        bank_data[recv]["balance"] += amt
        transaction_history[user].append(f"Transfer - {amt} to {recv}")
        transaction_history[recv].append(f"Transfer + {amt} from {user}")
        print("Transfer successful.")

def show_transactions(user):
    if not transaction_history[user]:
        print("No transactions.")
    else:
        for t in transaction_history[user]:
            print(t)

def user_menu(user):
    while True:
        print(f"\nLogged in: {user}")
        print("1 Deposit  2 Withdraw  3 Balance  4 Transfer  5 History  6 Logout")
        c = input("Choice: ")
        if c == "1": deposit(user)
        elif c == "2": withdraw(user)
        elif c == "3": check_balance(user)
        elif c == "4": transfer(user)
        elif c == "5": show_transactions(user)
        elif c == "6": break
        else: print("Invalid choice.")

def menu():
    while True:
        print("\nBANK MENU: 1 Create  2 Login  3 Exit")
        c = input("Choice: ")
        if c == "1": create_account()
        elif c == "2":
            u = login()
            if u: user_menu(u)
        elif c == "3":
            print("Goodbye.")
            break
        else:
            print("Invalid.")

menu()