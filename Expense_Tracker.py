expenses = []

while True:
    print("\n--- Expense Tracker ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        date = input("Enter date (DD-MM-YYYY): ")
        category = input("Enter category (Food/Travel/etc): ")
        amount = float(input("Enter amount: "))

        expense = {
            "date": date,
            "category": category,
            "amount": amount
        }

        expenses.append(expense)
        print("Expense added successfully!")

    elif choice == "2":
        if not expenses:
            print("No expenses found.")
        else:
            print("\nDate\t\tCategory\tAmount")
            for e in expenses:
                print(e["date"], "\t", e["category"], "\t\t", e["amount"])

    elif choice == "3":
        total = 0
        for e in expenses:
            total += e["amount"]
        print("Total Expense:", total)

    elif choice == "4":
        print("Thank you! Exiting program.")
        break

    else:
        print("Invalid choice. Try again.")