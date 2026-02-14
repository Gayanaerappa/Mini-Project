events = []

def add_event():
    name = input("Enter Event Name: ")
    client = input("Enter Client Name: ")
    guests = int(input("Enter Number of Guests: "))
    cost_per_guest = float(input("Enter Cost Per Guest: "))
    advance = float(input("Enter Advance Payment: "))

    total_cost = guests * cost_per_guest
    balance = total_cost - advance

    event = {
        "Event": name,
        "Client": client,
        "Guests": guests,
        "TotalCost": total_cost,
        "Advance": advance,
        "Balance": balance
    }

    events.append(event)
    print(" Event Added Successfully")

def view_events():
    if not events:
        print("⚠ No events available")
        return

    print("\n--- Event Details ---")
    print("Event\tClient\tTotal\tAdvance\tBalance")

    for e in events:
        print(e["Event"], "\t", e["Client"], "\t",
              e["TotalCost"], "\t", e["Advance"], "\t", e["Balance"])

def total_revenue():
    revenue = 0
    for e in events:
        revenue += e["Advance"]   # Company received only advance so far

    print(" Revenue Collected (Advance Only):", revenue)

def search_event():
    search = input("Enter Event Name: ")

    for e in events:
        if e["Event"].lower() == search.lower():
            print("\n Event Found")
            print("Client:", e["Client"])
            print("Total Cost:", e["TotalCost"])
            print("Advance Paid:", e["Advance"])
            print("Balance Due:", e["Balance"])
            return

    print(" Event Not Found")

# ===== MENU =====

while True:
    print("\n===== Event Management System =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Revenue Collected")
    print("4. Search Event")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_event()
    elif choice == "2":
        view_events()
    elif choice == "3":
        total_revenue()
    elif choice == "4":
        search_event()
    elif choice == "5":
        print(" Exiting Program")
        break
    else:
        print("❌ Invalid Choice")
