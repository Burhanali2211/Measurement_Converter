import sys

# Main menu
def menu():
    print("\nWelcome to the Measurement Converter!")
    print("1. Length")
    print("2. Breadth")
    print("3. Height")
    print("4. Exit")

# Length conversion
def length():
    print("\nLength Conversions:")
    print("1. Meters to Centimeters")
    print("2. Kilometers to Meters")
    print("3. Meters to Inches")
    print("4. Back to Main Menu")

    try:
        choice = int(input("Choose an option (1-4): "))
        if choice == 1:
            meters = float(input("Enter value in meters: "))
            print(f"{meters} meters = {meters * 100} centimeters.")
        elif choice == 2:
            kilometers = float(input("Enter value in kilometers: "))
            print(f"{kilometers} kilometers = {kilometers * 1000} meters.")
        elif choice == 3:
            meters = float(input("Enter value in meters: "))
            print(f"{meters} meters = {meters * 39.3701} inches.")
        elif choice == 4:
            return  # Return to the main menu
        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Breadth conversion
def breadth():
    print("\nBreadth Conversions:")
    print("1. Meters to Feet")
    print("2. Feet to Inches")
    print("3. Back to Main Menu")

    try:
        choice = int(input("Choose an option (1-3): "))
        if choice == 1:
            meters = float(input("Enter value in meters: "))
            print(f"{meters} meters = {meters * 3.28084} feet.")
        elif choice == 2:
            feet = float(input("Enter value in feet: "))
            print(f"{feet} feet = {feet * 12} inches.")
        elif choice == 3:
            return
        else:
            print("Invalid choice! Please try again.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

# Main program loop
while True:
    menu()
    try:
        user_menu = int(input("What do you want to convert (1-4): "))
        if user_menu == 1:
            length()
        elif user_menu == 2:
            breadth()
        elif user_menu == 3:
            print("\nHeight conversion coming soon!")  # Placeholder for Height
        elif user_menu == 4:
            print("Thank you for using the Measurement Converter. Goodbye!")
            break
        else:
            print("Invalid choice! Please choose a valid option.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
