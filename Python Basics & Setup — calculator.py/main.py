from converters import *

while True:
    print("\nConverter Menu")
    print("1. KM to Miles")
    print("2. Celsius to Fahrenheit")
    print("3. KG to Pounds")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        km = float(input("Enter kilometers: "))
        print(f"Miles: {km_to_miles(km):.2f}")

    elif choice == "2":
        c = float(input("Enter Celsius: "))
        print(f"Fahrenheit: {celsius_to_fahrenheit(c):.2f}")

    elif choice == "3":
        kg = float(input("Enter KG: "))
        print(f"Pounds: {kg_to_pounds(kg):.2f}")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")