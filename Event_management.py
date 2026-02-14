events = []

def add_event():
    name = input("Enter Event Name: ")
    client = input("Enter Client Name: ")
    guests = int(input("Enter Number of Guests: "))
    cost_per_guest = float(input("Enter Cost Per Guest: "))

    total_cost = guests * cost_per_guest

    event = {
        "Event": name,
        "Client": client,
        "Guests": guests,
        "CostPerGuest": cost_per_guest,
        "TotalCost": total_cost
    }

    events.append(event)
    print("✅ Event Added Successfully")

def view_events():
    if not events:
        print("⚠ No events available")
        return

    print("\n--- Event List ---")
    print("Event\tClient\tGuests\tTotal Cost")

    for e in events:
        print(e["Event"], "\t", e["Client"], "\t",
              e["Guests"], "\t", e["TotalCost"])

def total_revenue():
    revenue = 0
    for e in events:
        revenue += e["TotalCost"]

    print("💰 Total Revenue:", revenue)

def search_event():
    search = input("Enter Event Name to Search: ")

    for e in events:
        if e["Event"].lower() == search.lower():
            print("\n✅ Event Found")
            print(e)
            return

    print("❌ Event Not Found")

# ===== MAIN MENU =====

while True:
    print("\n===== Event Management System =====")
    print("1. Add Event")
    print("2. View Events")
    print("3. Total Revenue")
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
        print("👋 Exiting Program")
        break
    else:
        print("❌ Invalid Choice")
