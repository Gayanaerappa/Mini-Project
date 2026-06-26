# Employee Management System

import os

FILE = "employees.txt"


def add_employee():
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    department = input("Enter Department: ")
    salary = input("Enter Salary: ")

    with open(FILE, "a") as f:
        f.write(f"{emp_id},{name},{department},{salary}\n")

    print("Employee added successfully!\n")


def view_employee():
    if not os.path.exists(FILE):
        print("No records found\n")
        return

    print("\n--- Employee Details ---")

    with open(FILE, "r") as f:
        for line in f:
            emp_id, name, dept, salary = line.strip().split(",")
            print("ID:", emp_id)
            print("Name:", name)
            print("Department:", dept)
            print("Salary:", salary)
            print("-------------------")


def search_employee():
    search_id = input("Enter Employee ID: ")
    found = False

    with open(FILE, "r") as f:
        for line in f:
            data = line.strip().split(",")

            if data[0] == search_id:
                print("\nEmployee Found")
                print("ID:", data[0])
                print("Name:", data[1])
                print("Department:", data[2])
                print("Salary:", data[3])
                found = True

    if not found:
        print("Employee not found")


def delete_employee():
    delete_id = input("Enter Employee ID to delete: ")

    if not os.path.exists(FILE):
        print("No records")
        return

    with open(FILE, "r") as f:
        records = f.readlines()

    with open(FILE, "w") as f:
        for line in records:
            if line.split(",")[0] != delete_id:
                f.write(line)

    print("Employee deleted successfully")


while True:

    print("\n===== Employee Management System =====")
    print("1. Add Employee")
    print("2. View Employee")
    print("3. Search Employee")
    print("4. Delete Employee")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_employee()

    elif choice == "2":
        view_employee()

    elif choice == "3":
        search_employee()

    elif choice == "4":
        delete_employee()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice")
