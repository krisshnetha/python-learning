contacts = {}

while True:
    print("\n1. Add Contact")
    print("2. Update Contact")
    print("3. Delete Contact")
    print("4. Search Contact")
    print("5. Show All Contacts")
    print("6. Find Duplicate Numbers")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone

    elif choice == "2":
        name = input("Name to update: ")
        if name in contacts:
            contacts[name] = input("New phone number: ")

    elif choice == "3":
        name = input("Name to delete: ")
        contacts.pop(name, None)

    elif choice == "4":
        name = input("Search name: ")
        print(contacts.get(name, "Not found"))

    elif choice == "5":
        for name, phone in contacts.items():
            print(name, phone)

    elif choice == "6":
        numbers = list(contacts.values())
        duplicates = {num for num in numbers if numbers.count(num) > 1}
        print("Duplicate numbers:", duplicates)

    elif choice == "7":
        break