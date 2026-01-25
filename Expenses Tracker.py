# Expense Tracker with Monthly Report

expenses = []

def add_expense():
    amount = float(input("Enter amount: "))
    category = input("Enter category (Food, Travel, Shopping, etc): ")
    note = input("Enter note: ")
    month = input("Enter month (Jan, Feb, Mar, etc): ")

    expense = {
        "amount": amount,
        "category": category,
        "note": note,
        "month": month
    }

    expenses.append(expense)
    print("Expense added successfully!")

def view_expenses():
    if len(expenses) == 0:
        print("No expenses recorded.")
    else:
        print("\n--- All Expenses ---")
        for i, exp in enumerate(expenses, start=1):
            print(f"{i}. {exp['month']} - {exp['category']} - {exp['amount']} - {exp['note']}")

def total_spending():
    total = 0
    for exp in expenses:
        total += exp["amount"]
    print("Total Spending:", total)

def monthly_report():
    month_name = input("Enter month to view report: ")
    total = 0
    found = False

    print(f"\n--- {month_name} Report ---")
    for exp in expenses:
        if exp["month"].lower() == month_name.lower():
            print(f"{exp['category']} - {exp['amount']} - {exp['note']}")
            total += exp["amount"]
            found = True

    if not found:
        print("No expenses found for this month.")
    else:
        print("Total for", month_name, ":", total)

# Main Program
while True:
    print("\n1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Monthly Report")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()

    elif choice == "2":
        view_expenses()

    elif choice == "3":
        total_spending()

    elif choice == "4":
        monthly_report()

    elif choice == "5":
        print("Thank you for using Expense Tracker!")
        break

    else:
        print("Invalid choice!")