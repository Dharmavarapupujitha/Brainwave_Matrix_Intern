# atm.py

balance = 1000  # Initial balance

def check_balance():
    print(f"\nYour balance is ₹{balance}\n")

def deposit():
    global balance
    amount = float(input("Enter deposit amount: ₹"))
    balance += amount
    print(f"₹{amount} deposited successfully.")

def withdraw():
    global balance
    amount = float(input("Enter withdrawal amount: ₹"))
    if amount > balance:
        print("Insufficient funds!")
    else:
        balance -= amount
        print(f"₹{amount} withdrawn successfully.")

def atm_menu():
    while True:
        print("\n===== ATM Menu =====")
        print("1. Check Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            check_balance()
        elif choice == '2':
            deposit()
        elif choice == '3':
            withdraw()
        elif choice == '4':
            print("Thank you for using the ATM!")
            break
        else:
            print("Invalid option. Try again.")

# Run the ATM
atm_menu()
