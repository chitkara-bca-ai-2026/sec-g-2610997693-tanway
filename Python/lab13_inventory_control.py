inventory = ["Notebook", "Pen", "Eraser", "Ruler"]

print("=" * 50)
print("            INVENTORY CONTROL SYSTEM")
print("=" * 50)

while True:
    print()
    print("Select an operation:")
    print("1. View Inventory")
    print("2. Add Item")
    print("3. Remove Item")
    print("4. Sort Inventory")
    print("5. Exit")
    print()

    choice = input("Enter your choice (1-5): ").strip()

    if choice == "1":
        print()
        print("--- Current Inventory ---")
        if not inventory:
            print("Inventory is empty.")
        else:
            for i, item in enumerate(inventory, 1):
                print(f"{i}. {item}")

    elif choice == "2":
        item = input("Enter item name to add: ").strip()
        inventory.append(item)
        print(f'[SUCCESS] "{item}" added to inventory.')

    elif choice == "3":
        item = input("Enter item name to remove: ").strip()
        if item in inventory:
            inventory.remove(item)
            print(f'[SUCCESS] "{item}" removed from inventory.')
        else:
            print(f'[ERROR] "{item}" not found in inventory.')

    elif choice == "4":
        inventory.sort()
        print()
        print("[SUCCESS] Inventory sorted alphabetically.")
        print("Updated Inventory:")
        for i, item in enumerate(inventory, 1):
            print(f"{i}. {item}")

    elif choice == "5":
        print()
        print("Thank you for using the Inventory Control System. Goodbye!")
        break

    else:
        print()
        print("[ERROR] Invalid choice. Please enter a number between 1 and 5.")
