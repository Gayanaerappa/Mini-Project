# ATM Mini Project

balance = 10000   # initial balance
pin = "1234"

print("===== Welcome to Python ATM =====")

user_pin = input("Enter your PIN: ")

if user_pin == pin:

    while True:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice: ")

        # Check Balance
        if choice == "1":
            print("Your balance is:", balance)

        # Deposit
        elif choice == "2":
            amount = int(input("Enter amount to deposit: "))
            balance += amount
            print("Deposit successful!")
            print("Updated balance:", balance)

        # Withdraw
        elif choice == "3":
            amount = int(input("Enter amount to withdraw: "))

            if amount <= balance:
                balance -= amount
                print("Please collect your cash")
                print("Remaining balance:", balance)
            else:
                print("Insufficient balance!")

        # Exit
        elif choice == "4":
            print("Thank you for using ATM")
            break

        else:
            print("Invalid choice")

else:
    print("Wrong PIN. Access Denied!")
