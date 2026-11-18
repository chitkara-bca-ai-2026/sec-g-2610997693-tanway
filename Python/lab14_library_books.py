books = [
    ("Python Crash Course", "Eric Matthes", "2019", "Programming"),
    ("Automate the Boring Stuff", "Al Sweigart", "2020", "Programming"),
    ("Artificial Intelligence: A Modern Approach", "Stuart Russell", "2021", "AI"),
    ("Clean Code", "Robert C. Martin", "2008", "Software Engineering"),
]

library_categories = {category for _, _, _, category in books}
student_wishlist = {"AI", "Cloud Computing", "Robotics", "Cybersecurity"}

print("==================================================")
print("         LIBRARY BOOK & CATEGORY MANAGER")
print("==================================================")

while True:
    print()
    print("Select an operation:")
    print("1. View Cataloged Books")
    print("2. Add New Book Record")
    print("3. View Unique Library Categories")
    print("4. Add Category to Student Wishlist")
    print("5. Run Category Gap Analysis")
    print("6. Exit")
    print()

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        print()
        print("--- Current Library Catalog (Fixed Records) ---")
        for i, book in enumerate(books, 1):
            title, author, year, category = book
            print(f'{i}. "{title}" by {author} ({year}) | Genre: {category}')
        print(f"Total Books: {len(books)}")

    elif choice == "2":
        print()
        print("--- Add New Book Record ---")
        title = input("Enter book title: ").strip()
        author = input("Enter author name: ").strip()
        year = input("Enter publication year: ").strip()
        category = input("Enter category/genre: ").strip()

        if title and author and year and category:
            books.append((title, author, year, category))
            library_categories.add(category)
            print()
            print(f'[SUCCESS] "{title}" added as an immutable catalog record.')
            print(f'[INFO] Category set updated with: "{category}"')

    elif choice == "3":
        print()
        print("--- Unique Categories Available in Library (Set) ---")
        for cat in sorted(library_categories):
            print(f" - {cat}")
        print(f"Total Unique Genres: {len(library_categories)}")

    elif choice == "4":
        print()
        print("--- Add to Student Wishlist ---")
        cat = input("Enter requested category: ").strip()
        if cat:
            student_wishlist.add(cat)
            print(f'[SUCCESS] "{cat}" added to student wishlist.')

    elif choice == "5":
        intersection = sorted(list(library_categories & student_wishlist))
        difference = sorted(list(student_wishlist - library_categories))
        union = sorted(list(library_categories | student_wishlist))

        print()
        print("============== CATEGORY GAP ANALYSIS ==============")
        print(f"Library Holdings (Set):  {sorted(list(library_categories))}")
        print(f"Student Wishlist (Set):  {sorted(list(student_wishlist))}")
        print("-" * 50)
        print("1. Already in Stock (Intersection &):")
        print(f"   {intersection}")
        print()
        print("2. Purchase Order Needed (Difference -):")
        print(f"   {difference}")
        print()
        print("3. Full Combined Genre Coverage (Union |):")
        print(f"   {union}")
        print("=" * 50)

    elif choice == "6":
        print()
        print("Thank you for using the Library Manager. Goodbye!")
        break

    else:
        print()
        print("[ERROR] Invalid choice. Please enter a number between 1 and 6.")
