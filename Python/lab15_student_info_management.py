students = {
    "101": {"Name": "Aman", "Branch": "BCA AI", "Semester": "1", "Marks": [85, 90, 78]},
    "102": {"Name": "Riya", "Branch": "BCA AI", "Semester": "1", "Marks": [92, 88, 95]},
    "103": {"Name": "Karan", "Branch": "BCA AI", "Semester": "1", "Marks": [74, 80, 82]},
}

print("==================================================")
print("       STUDENT INFORMATION MANAGEMENT SYSTEM")
print("==================================================")

while True:
    print()
    print("Select an operation:")
    print("1. View All Students")
    print("2. Search Student by Roll Number")
    print("3. Register New Student")
    print("4. Update Student Details")
    print("5. View Academic Performance")
    print("6. Delete Student Record")
    print("7. Exit")
    print()

    choice = input("Enter your choice (1-7): ").strip()

    if choice == "1":
        print()
        print("--- Enrolled Student Records ---")
        for roll, info in students.items():
            print(f"Roll No: {roll:<5} | Name: {info['Name']:<10} | Branch: {info['Branch']:<9} | Sem: {info['Semester']} | Marks: {info['Marks']}")
        print(f"Total Enrolled Students: {len(students)}")

    elif choice == "2":
        roll = input("Enter Roll Number to search: ").strip()
        student = students.get(roll)
        if student:
            print()
            print(f"[FOUND] Record for Roll No {roll}:")
            print(f"  Name     : {student['Name']}")
            print(f"  Branch   : {student['Branch']}")
            print(f"  Semester : {student['Semester']}")
            print(f"  Marks    : {student['Marks']}")
        else:
            print()
            print(f"[ERROR] Student with Roll Number '{roll}' not found.")

    elif choice == "3":
        print()
        print("--- Register New Student ---")
        roll = input("Enter Roll Number: ").strip()
        if roll in students:
            print(f"[ERROR] Student with Roll Number '{roll}' already exists.")
        else:
            name = input("Enter Student Name: ").strip()
            branch = input("Enter Branch (e.g. BCA AI): ").strip()
            semester = input("Enter Semester: ").strip()
            print("Enter marks obtained in 3 subjects:")
            m1 = int(input("  Subject 1: "))
            m2 = int(input("  Subject 2: "))
            m3 = int(input("  Subject 3: "))
            students[roll] = {
                "Name": name,
                "Branch": branch,
                "Semester": semester,
                "Marks": [m1, m2, m3]
            }
            print()
            print(f"[SUCCESS] Student '{name}' (Roll No: {roll}) registered successfully.")

    elif choice == "4":
        roll = input("Enter Roll Number to update: ").strip()
        student = students.get(roll)
        if not student:
            print(f"[ERROR] Student with Roll Number '{roll}' not found.")
        else:
            print(f"Current details for {student['Name']} (Roll {roll}):")
            print(f" 1. Branch: {student['Branch']} | 2. Semester: {student['Semester']}")
            field_choice = input("Choose field to update (1 for Branch, 2 for Semester): ").strip()
            if field_choice == "1":
                new_branch = input("Enter new branch: ").strip()
                student["Branch"] = new_branch
                print(f"[SUCCESS] Branch updated to '{new_branch}'.")
            elif field_choice == "2":
                new_sem = input("Enter new semester: ").strip()
                student["Semester"] = new_sem
                print(f"[SUCCESS] Semester updated to '{new_sem}'.")
            else:
                print("[ERROR] Invalid field selected.")

    elif choice == "5":
        roll = input("Enter Roll Number for Academic Performance: ").strip()
        student = students.get(roll)
        if not student:
            print(f"[ERROR] Student with Roll Number '{roll}' not found.")
        else:
            total = sum(student["Marks"])
            avg = total / len(student["Marks"])
            result = "PASS" if avg >= 40 else "FAIL"
            print()
            print("============== ACADEMIC REPORT ==============")
            print(f"Student Name : {student['Name']} (Roll: {roll})")
            print(f"Subject Marks: {student['Marks']}")
            print(f"Total Marks  : {total} / {len(student['Marks']) * 100}")
            print(f"Average Marks: {avg:.2f}%")
            print(f"Final Result : {result}")
            print("==============================================")

    elif choice == "6":
        roll = input("Enter Roll Number to delete: ").strip()
        deleted = students.pop(roll, None)
        if deleted:
            print()
            print(f"[SUCCESS] Record for '{deleted['Name']}' (Roll No: {roll}) deleted successfully.")
        else:
            print()
            print(f"[ERROR] Student with Roll Number '{roll}' not found.")

    elif choice == "7":
        print()
        print("Thank you for using Student Information System. Goodbye!")
        break

    else:
        print()
        print("[ERROR] Invalid choice. Please enter a number between 1 and 7.")
