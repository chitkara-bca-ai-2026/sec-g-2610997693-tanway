import math

print("=" * 50)
print("           ENGINEERING CALCULATION TOOL")
print("=" * 50)
val = float(input("Enter a numerical value: "))
exp = float(input("Enter an exponent: "))
dec = float(input("Enter a decimal measurement: "))

power_val = math.pow(val, exp)
sqrt_val = math.sqrt(val)
ceil_val = math.ceil(dec)
floor_val = math.floor(dec)

print()
print("--- Results ---")
print(f"  Value              : {val}")
print(f"  Exponent           : {exp}")
print(f"  Power (pow)        : {power_val}")
print(f"  Square Root (sqrt) : {sqrt_val:.4f}")
print(f"  Decimal Value      : {dec}")
print(f"  Ceil Value         : {ceil_val}")
print(f"  Floor Value        : {floor_val}")
print("=" * 50)
