balance = 5000

while True:
    print("\n1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        print("Balance:", balance)

    elif choice == "2":
        amount = int(input("Enter amount: "))
        balance += amount
        print("Deposited")

    elif choice == "3":
        amount = int(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawn")
        else:
            print("Insufficient balance!")

    elif choice == "4":
        break

    else:
        print("Invalid choice")