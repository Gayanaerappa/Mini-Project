phonebook = {}

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    ch = input("Enter choice: ")

    if ch == "1":
        name = input("Enter name: ")
        number = input("Enter number: ")
        phonebook[name] = number

    elif ch == "2":
        print(phonebook)

    elif ch == "3":
        name = input("Enter name to search: ")
        print(phonebook.get(name, "Contact not found"))

    elif ch == "4":
        break