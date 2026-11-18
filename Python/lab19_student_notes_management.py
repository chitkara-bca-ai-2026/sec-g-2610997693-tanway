import os

def write_notes(filename, content):
    with open(filename, "w") as f:
        f.write(content)
    print(f"[SUCCESS] Notes successfully saved to '{filename}'.")

def read_notes(filename):
    if not os.path.exists(filename):
        return f"[INFO] No notes file found at '{filename}'."
    with open(filename, "r") as f:
        return f.read()

filename = "notes.txt"

print("--------------------------------------------------")
print("          STUDENT NOTES MANAGEMENT SYSTEM")
print("--------------------------------------------------")

while True:
    print()
    print("Select an operation:")
    print("1. Write / Save Notes")
    print("2. View Saved Notes")
    print("3. Exit")
    print()

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        content = input("Enter notes to save: ")
        write_notes(filename, content)

    elif choice == "2":
        content = read_notes(filename)
        print()
        print(f"--- Notes Content ({filename}) ---")
        print(content)

    elif choice == "3":
        print("Thank you for using the Notes Management System. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 3.")