# Smart Agriculture Mini Project

farmers = []
crops = []

# ------------------------
# Farmer Registration
# ------------------------
def register_farmer():
    name = input("Enter farmer name: ")
    village = input("Enter village: ")

    farmer = {
        "name": name,
        "village": village
    }

    farmers.append(farmer)
    print("Farmer registered successfully!")

# ------------------------
# Add Crop
# ------------------------
def add_crop():
    crop_name = input("Enter crop name: ")
    season = input("Enter season (Kharif/Rabi/Zaid): ")
    fertilizer = input("Enter recommended fertilizer: ")

    crop = {
        "crop": crop_name,
        "season": season,
        "fertilizer": fertilizer
    }

    crops.append(crop)
    print("Crop added successfully!")

# ------------------------
# View Crops
# ------------------------
def view_crops():
    print("\n--- Crop Details ---")
    if len(crops) == 0:
        print("No crops available.")
    else:
        for c in crops:
            print(f"Crop: {c['crop']} | Season: {c['season']} | Fertilizer: {c['fertilizer']}")

# ------------------------
# Fertilizer Recommendation
# ------------------------
def fertilizer_recommend():
    name = input("Enter crop name: ")

    found = False
    for c in crops:
        if c["crop"].lower() == name.lower():
            print("Recommended Fertilizer:", c["fertilizer"])
            found = True

    if not found:
        print("Crop not found.")

# ------------------------
# Weather Tips
# ------------------------
def weather_tips():
    print("\n--- Weather Tips ---")
    print(" Water crops early morning")
    print(" Ensure proper drainage during heavy rain")
    print(" Protect crops from frost")

# ------------------------
# Main Menu
# ------------------------
while True:
    print("\n===== SMART AGRICULTURE SYSTEM =====")
    print("1. Register Farmer")
    print("2. Add Crop")
    print("3. View Crops")
    print("4. Fertilizer Recommendation")
    print("5. Weather Tips")
    print("6. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_farmer()
    elif choice == "2":
        add_crop()
    elif choice == "3":
        view_crops()
    elif choice == "4":
        fertilizer_recommend()
    elif choice == "5":
        weather_tips()
    elif choice == "6":
        print("Thank you!")
        break
    else:
        print("Invalid choice")
