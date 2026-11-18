def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return None
    return a / b

def modulus(a, b):
    if b == 0:
        return None
    return a % b

def power(base, exp=2):
    return base ** exp

def format_number(n):
    if isinstance(n, (int, float)):
        if n == int(n):
            return int(n)
        return n
    return n

history = []

print("--------------------------------------------------")
print("       ENTERPRISE MODULAR UTILITY CALCULATOR")
print("--------------------------------------------------")

while True:
    print()
    print("Select an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus / Remainder (%)")
    print("6. Power / Exponentiation (Default: Square)")
    print("7. View Calculation History")
    print("8. Exit")
    print()

    choice = input("Enter your choice (1-8): ").strip()

    if choice in ("1", "2", "3", "4", "5"):
        a_raw = float(input("Enter first number: "))
        b_raw = float(input("Enter second number: "))
        a = format_number(a_raw)
        b = format_number(b_raw)

        if choice == "1":
            res = format_number(add(a_raw, b_raw))
            entry = f"{a} + {b} = {res}"
            history.append(entry)
            print(f"[RESULT] {entry}")
        elif choice == "2":
            res = format_number(subtract(a_raw, b_raw))
            entry = f"{a} - {b} = {res}"
            history.append(entry)
            print(f"[RESULT] {entry}")
        elif choice == "3":
            res = format_number(multiply(a_raw, b_raw))
            entry = f"{a} * {b} = {res}"
            history.append(entry)
            print(f"[RESULT] {entry}")
        elif choice == "4":
            calc = divide(a_raw, b_raw)
            if calc is None:
                print("[ERROR] Cannot divide by zero.")
            else:
                res = format_number(calc)
                entry = f"{a} / {b} = {res}"
                history.append(entry)
                print(f"[RESULT] {entry}")
        elif choice == "5":
            calc = modulus(a_raw, b_raw)
            if calc is None:
                print("[ERROR] Modulo by zero is not allowed.")
            else:
                res = format_number(calc)
                entry = f"{a} % {b} = {res}"
                history.append(entry)
                print(f"[RESULT] {entry}")

    elif choice == "6":
        b_raw = float(input("Enter base number: "))
        exp_in = input("Enter exponent (press Enter for default 2): ").strip()
        base_val = format_number(b_raw)
        if exp_in == "":
            res = format_number(power(b_raw))
            entry = f"{base_val} ^ 2 = {res}"
        else:
            e_raw = float(exp_in)
            exp_val = format_number(e_raw)
            res = format_number(power(b_raw, e_raw))
            entry = f"{base_val} ^ {exp_val} = {res}"
        history.append(entry)
        print(f"[RESULT] {entry}")

    elif choice == "7":
        print()
        print("--- Calculation History ---")
        if not history:
            print("No calculations performed yet.")
        else:
            for idx, item in enumerate(history, 1):
                print(f"{idx}. {item}")

    elif choice == "8":
        print()
        print("Thank you for using the Utility Calculator. Goodbye!")
        break

    else:
        print()
        print("[ERROR] Invalid choice. Please enter a number between 1 and 8.")
