n = int(input("Enter the number of rows: "))

print("Pattern 1: Star Triangle")
print("-" * 35)
for i in range(1, n + 1):
    for j in range(i):
        if j == i - 1:
            print("*", end="")
        else:
            print("* ", end="")
    print()

print()
print("Pattern 2: Number Triangle")
print("-" * 35)
for i in range(1, n + 1):
    for j in range(1, i + 1):
        if j == i:
            print(j, end="")
        else:
            print(f"{j} ", end="")
    print()

print()
print("Pattern 3: Inverted Star Triangle")
print("-" * 35)
for i in range(n, 0, -1):
    for j in range(i):
        if j == i - 1:
            print("*", end="")
        else:
            print("* ", end="")
    print()

print()
print("Pattern 4: Pyramid")
print("-" * 35)
for i in range(n):
    for _ in range((n - 1 - i) * 2):
        print(" ", end="")
    for j in range(2 * i + 1):
        if j == 2 * i:
            print("*", end="")
        else:
            print("* ", end="")
    print()
