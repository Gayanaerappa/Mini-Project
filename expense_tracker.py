# Personal Expense Tracker - Mini Project

expenses = []

def add_expense():
    name = input("Enter expense name: ")
    amount = float(input("Enter amount: "))
    
    expense = {"name": name, "amount": amount}
    expenses.append(expense)
    
    print("✅ Expense added successfully!\n")

def view_expenses():
    if len(expenses) == 0:
        print("⚠ No expenses recorded.\n")
        return
    
    print("\n📋 All Expenses:")
    for i, exp in enumerate(expenses, start=1):
        print(f"{i}. {exp['name']} - ₹{exp['amount']}")
    print()

def total_spending():
    total = sum(exp["amount"] for exp in expenses)
    print(f"\n💰 Total Spending: ₹{total}\n")

def highest_expense():
    if len(expenses) == 0:
        print("⚠ No expenses recorded.\n")
        return
    
    highest = max(expenses, key=lambda x: x["amount"])
    print(f"\n🔥 Highest Expense: {highest['name']} - ₹{highest['amount']}\n")

def menu():
    print("====== Expense Tracker ======")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Total Spending")
    print("4. Highest Expense")
    print("5. Exit")

while True:
    menu()
    choice = input("Choose an option: ")
    
    if choice == "1":
        add_expense()
    elif choice == "2":
        view_expenses()
    elif choice == "3":
        total_spending()
    elif choice == "4":
        highest_expense()
    elif choice == "5":
        print("👋 Exiting program. Goodbye!")
        break
    else:
        print("❌ Invalid choice. Try again.\n")
