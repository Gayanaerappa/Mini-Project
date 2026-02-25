import os

FILE_NAME = "students.txt"

# Add Student
def add_student():
    name = input("Enter student name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{age},{course}\n")

    print("✅ Student added successfully!\n")


# View Students
def view_students():
    if not os.path.exists(FILE_NAME):
        print("No student records found.\n")
        return

    with open(FILE_NAME, "r") as file:
        students = file.readlines()

    if not students:
        print("No student records found.\n")
        return

    print("\n📋 Student List:")
    for i, student in enumerate(students, start=1):
        name, age, course = student.strip().split(",")
        print(f"{i}. Name: {name}, Age: {age}, Course: {course}")
    print()


# Search Student
def search_student():
    name_to_search = input("Enter student name to search: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    found = False
    with open(FILE_NAME, "r") as file:
        for student in file:
            name, age, course = student.strip().split(",")
            if name.lower() == name_to_search.lower():
                print(f"✅ Found: Name: {name}, Age: {age}, Course: {course}\n")
                found = True
                break

    if not found:
        print("❌ Student not found.\n")


# Delete Student
def delete_student():
    name_to_delete = input("Enter student name to delete: ")

    if not os.path.exists(FILE_NAME):
        print("No records found.\n")
        return

    updated_students = []
    found = False

    with open(FILE_NAME, "r") as file:
        for student in file:
            name, age, course = student.strip().split(",")
            if name.lower() != name_to_delete.lower():
                updated_students.append(student)
            else:
                found = True

    with open(FILE_NAME, "w") as file:
        file.writelines(updated_students)

    if found:
        print("🗑️ Student deleted successfully!\n")
    else:
        print("❌ Student not found.\n")


# Main Menu
def main():
    while True:
        print("====== Student Management System ======")
        print("1. Add Student")
        print("2. View Students")
        print("3. Search Student")
        print("4. Delete Student")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            delete_student()
        elif choice == "5":
            print("👋 Exiting program...")
            break
        else:
            print("Invalid choice. Try again.\n")


if __name__ == "__main__":
    main()
