students = []

n = int(input("Enter number of students: "))

for i in range(n):
    student = {}
    student["name"] = input("Enter student name: ")
    student["maths"] = int(input("Maths marks: "))
    student["science"] = int(input("Science marks: "))
    student["english"] = int(input("English marks: "))

    student["total"] = student["maths"] + student["science"] + student["english"]
    student["average"] = student["total"] / 3

    if student["average"] >= 40:
        student["result"] = "Pass"
    else:
        student["result"] = "Fail"

    students.append(student)
print("\n--- Student Results ---")
for s in students:
    print(s["name"], "| Total:", s["total"], "| Avg:", s["average"], "|", s["result"])
