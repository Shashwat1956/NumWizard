print("Welcome to Calculator 1956")
print("--------------------------")
print("Operations Available:")
print("--------------------------")

while True:
    try:
        a = float(input("Enter the first number: "))
        b = float(input("Enter the second number: "))
    except ValueError:
        print("Invalid input! Please enter valid numbers.")
        continue

    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        result = a + b
        operation = "Addition"
    elif choice == '2':
        result = a - b
        operation = "Subtraction"
    elif choice == '3':
        result = a * b
        operation = "Multiplication"
    elif choice == '4':
        if b != 0:
            result = a / b
            operation = "Division"
        else:
            print("Error: Division by zero!")
            continue
    elif choice == '5':
        print("Exiting calculator...")
        break
    else:
        print("Invalid choice! Please enter a number from 1 to 5.")
        continue

    print(f"\n{operation} result: {result}")
    print("----------------------------")

    while True:
        try:
            cont = input("Do you want to continue? (yes/no): ").lower()
            if cont == 'yes' or cont == 'no':
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no'.")
        except ValueError:
            print("Invalid input! Please enter 'yes' or 'no'.")

    if cont == 'no':
        print("Exiting calculator...")
        break

print("Thank you for using Calculator 1956!")
