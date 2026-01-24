books = ["Python", "Java", "C", "C++", "Data Science"]

issued_books = []

while True:
    print("\n LIBRARY MANAGEMENT SYSTEM")
    print("1. View Available Books")
    print("2. Issue Book")
    print("3. Return Book")
    print("4. Exit")

    choice = input("Enter your choice: ")

    # 1. View Available Books
    if choice == "1":
        if not books:
            print(" No books available")
        else:
            print("\nAvailable Books:")
            for book in books:
                print("-", book)

    # 2. Issue Book
    elif choice == "2":
        book_name = input("Enter book name to issue: ")

        if book_name in books:
            books.remove(book_name)
            issued_books.append(book_name)
            print(f" '{book_name}' issued successfully")
        else:
            print(" Book not available")

    # 3. Return Book
    elif choice == "3":
        book_name = input("Enter book name to return: ")

        if book_name in issued_books:
            issued_books.remove(book_name)
            books.append(book_name)
            print(f" '{book_name}' returned successfully")
        else:
            print(" This book was not issued")

    # 4. Exit
    elif choice == "4":
        print(" Exiting Library System")
        break

    else:
        print(" Invalid choice. Try again.")