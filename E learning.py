#E-Learning & Medical Assistant System For Physically Impaired Students
students = []
doctors = []
teachers = []

medical_advice = []
sign_lessons = []
medicines = []   # new medicine module

# ------------------------
# Student Registration
# ------------------------
def register_student():
    name = input("Enter student name: ")
    challenge = input("Enter challenge type (Hearing / Vision / Physical): ")

    student = {
        "name": name,
        "challenge": challenge
    }

    students.append(student)
    print("Student registered successfully!")

# ------------------------
# Doctor Module
# ------------------------
def doctor_register():
    name = input("Enter doctor name: ")
    doctors.append(name)
    print("Doctor registered!")

def add_medical_advice():
    advice = input("Enter medical advice: ")
    medical_advice.append(advice)
    print("Advice added!")

def add_medicine():
    med_name = input("Enter medicine name: ")
    dosage = input("Enter dosage (e.g., 1 tablet morning): ")

    medicine = {
        "name": med_name,
        "dosage": dosage
    }

    medicines.append(medicine)
    print("Medicine added successfully!")

def view_medical_advice():
    print("\n--- Medical Advice ---")
    for adv in medical_advice:
        print("-", adv)

# ------------------------
# Teacher Module
# ------------------------
def teacher_register():
    name = input("Enter teacher name: ")
    teachers.append(name)
    print("Teacher registered!")

def add_sign_lesson():
    lesson = input("Enter sign language lesson topic: ")
    sign_lessons.append(lesson)
    print("Lesson added!")

def view_sign_lessons():
    print("\n--- Sign Language Lessons ---")
    for lesson in sign_lessons:
        print("-", lesson)

# ------------------------
# Medicine View
# ------------------------
def view_medicines():
    print("\n--- Medicines ---")
    if len(medicines) == 0:
        print("No medicines added.")
    else:
        for med in medicines:
            print(f"{med['name']} - {med['dosage']}")

# ------------------------
# Student Menu
# ------------------------
def student_menu():
    while True:
        print("\n1. View Sign Lessons")
        print("2. View Medical Advice")
        print("3. View Medicines")
        print("4. Back")

        ch = input("Enter choice: ")

        if ch == "1":
            view_sign_lessons()
        elif ch == "2":
            view_medical_advice()
        elif ch == "3":
            view_medicines()
        elif ch == "4":
            break
        else:
            print("Invalid choice")

# ------------------------
# Main Menu
# ------------------------
while True:
    print("\n===== MAIN MENU =====")
    print("1. Student Register")
    print("2. Doctor Register")
    print("3. Teacher Register")
    print("4. Doctor Add Advice")
    print("5. Doctor Add Medicine")
    print("6. Teacher Add Lesson")
    print("7. Student Login")
    print("8. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register_student()
    elif choice == "2":
        doctor_register()
    elif choice == "3":
        teacher_register()
    elif choice == "4":
        add_medical_advice()
    elif choice == "5":
        add_medicine()
    elif choice == "6":
        add_sign_lesson()
    elif choice == "7":
        student_menu()
    elif choice == "8":
        print("Thank you!")
        break
    else:
        print("Invalid option")
