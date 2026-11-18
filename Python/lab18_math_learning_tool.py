def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n - 1)

def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print("--------------------------------------------------")
print("             MATHEMATICS LEARNING TOOL")
print("--------------------------------------------------")

while True:
    print()
    print("Select an operation:")
    print("1. Calculate Factorial")
    print("2. Generate Fibonacci Series")
    print("3. Exit")
    print()

    choice = input("Enter choice (1-3): ").strip()

    if choice == "1":
        n = int(input("Enter a non-negative integer: "))
        if n < 0:
            print("[ERROR] Please enter a non-negative integer.")
        else:
            result = factorial(n)
            print(f"[RESULT] Factorial of {n} ({n}!) = {result}")

    elif choice == "2":
        terms = int(input("Enter number of terms to generate: "))
        if terms <= 0:
            print("[ERROR] Please enter a positive number of terms.")
        else:
            series = [fibonacci(i) for i in range(terms)]
            print(f"[RESULT] Fibonacci series ({terms} terms): {series}")

    elif choice == "3":
        print("Thank you for using the Mathematics Learning Tool. Goodbye!")
        break

    else:
        print("[ERROR] Invalid choice. Please enter a number between 1 and 3.")
