def calculate_results(marks):
    total = sum(marks)
    average = total / len(marks)
    return total, average

def display_student(roll, student):
    total, average = calculate_results(student["Marks"])
    print(f"Roll No: {roll} | Name: {student['Name']:<10} | Marks: {student['Marks']} | Total: {total} | Average: {average:.2f}%")

def add_student(records, roll, name, marks):
    if roll in records:
        print(f"[ERROR] Student with Roll Number '{roll}' already exists.")
    else:
        records[roll] = {"Name": name, "Marks": marks}
        print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) added successfully.")

students = {
    "101": {"Name": "Arman", "Marks": [85, 90, 78]},
    "102": {"Name": "Rishi", "Marks": [92, 88, 95]},
    "103": {"Name": "Rohan", "Marks": [74, 80, 82]},
}

print("--------------------------------------------------")
print("          STUDENT RECORDS MANAGEMENT SYSTEM")
print("--------------------------------------------------")

while True:
    print()
    print("Select an operation:")
    print("1. Display All Students")
    print("2. Add New Student")
    print("3. Search Student")
    print("4. Exit")
    print()

    choice = input("Enter choice (1-4): ").strip()

    if choice == "1":
        print("--- All Student Records ---")
        for roll, student in students.items():
            display_student(roll, student)
        print(f"Total Students: {len(students)}")

    elif choice == "2":
        print("--- Add New Student ---")
        roll = input("Enter Roll Number: ").strip()
        name = input("Enter Student Name: ").strip()
        print("Enter marks for 3 subjects:")
        m1 = int(input("  Subject 1: "))
        m2 = int(input("  Subject 2: "))
        m3 = int(input("  Subject 3: "))
        add_student(students, roll, name, [m1, m2, m3])

    elif choice == "3":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print("[RECORD FOUND]")
            display_student(roll, student)
        else:
            print(f"[ERROR] No student found with Roll Number '{roll}'.")

    elif choice == "4":
        print("Thank you for using the Student Records System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 4.")
