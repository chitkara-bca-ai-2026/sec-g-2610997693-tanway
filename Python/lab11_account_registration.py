username = input("Enter your username: ")
password = input("Enter your password: ")

print("=" * 50)
print("PASSWORD VALIDATION REPORT")
print("=" * 50)
print(f"Username: {username}")
print(f"Password: {'*' * len(password)}")

print()
print("--- Validation Rules ---")
is_len_valid = len(password) >= 8
status_len = "[PASS]" if is_len_valid else "[FAIL]"
print(f"{status_len} Minimum 8 characters ({len(password)} characters)")

has_digit = any(char.isdigit() for char in password)
status_digit = "[PASS]" if has_digit else "[FAIL]"
print(f"{status_digit} At least one digit")

has_upper = any(char.isupper() for char in password)
status_upper = "[PASS]" if has_upper else "[FAIL]"
print(f"{status_upper} At least one uppercase letter")

print()
print("--- Result ---")
if is_len_valid and has_digit and has_upper:
    print("Password is VALID!")
    print(f"Account created successfully for {username}!")
else:
    print("Password is INVALID!")

print()
print("=" * 50)
