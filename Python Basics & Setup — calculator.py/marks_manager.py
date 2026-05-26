students = []

while True:
    print("\n1. Add Student")
    print("2. Remove Student")
    print("3. Sort by Marks")
    print("4. Class Average")
    print("5. Topper")
    print("6. Lowest Scorer")
    print("7. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter student name: ")
        marks = float(input("Enter marks: "))
        students.append((name, marks))

    elif choice == "2":
        name = input("Enter name to remove: ")
        students = [s for s in students if s[0] != name]

    elif choice == "3":
        sorted_students = sorted(students, key=lambda x: x[1], reverse=True)
        print(sorted_students)

    elif choice == "4":
        if students:
            average = sum(mark for _, mark in students) / len(students)
            print(f"Average: {average:.2f}")

    elif choice == "5":
        topper = max(students, key=lambda x: x[1])
        print(f"Topper: {topper}")

    elif choice == "6":
        lowest = min(students, key=lambda x: x[1])
        print(f"Lowest Scorer: {lowest}")

    elif choice == "7":
        break