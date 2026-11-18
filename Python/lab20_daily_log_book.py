import os

def append_entry(filename, entry):
    with open(filename, "a") as f:
        f.write(entry + "\n")
    print(f"[SUCCESS] New entry logged to '{filename}'.")

def display_log(filename):
    if not os.path.exists(filename):
        print(f"[INFO] No log file found at '{filename}'.")
        return
    with open(filename, "r") as f:
        lines = [line.strip() for line in f if line.strip()]
    print("================ DAILY LOG BOOK ================")
    for line in lines:
        print(line)
    print()
    print(f"Total Logged Entries: {len(lines)}")
    print("================================================")

filename = "daily_log.txt"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("[01] 09:00 AM - System server startup verified.\n")
        f.write("[02] 10:30 AM - Morning attendance synchronized.\n")
        f.write("[03] 02:15 PM - Network security patch applied.\n")

print("--------------------------------------------------")
print("               OFFICE DAILY LOG BOOK")
print("--------------------------------------------------")

while True:
    print()
    print("Select an operation:")
    print("1. Add Log Entry")
    print("2. Display Complete Log")
    print("3. Exit")
    print()

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        entry = input("Enter log entry: ")
        append_entry(filename, entry)

    elif choice == "2":
        display_log(filename)

    elif choice == "3":
        print("Thank you for using the Daily Log Book. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 3.")
