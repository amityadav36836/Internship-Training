while True:
    print("\n--- Simple Calculator ---")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter your choice (1-5): ")

    
    if choice not in ['1', '2', '3', '4', '5']:
        print("Invalid choice! Please enter a number between 1-5.")
        continue

    if choice == '5':
        print("Exiting calculator... Goodbye!")
        break

    
    try:
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))
    except ValueError:
        print("Error: Please enter only numeric values!")
        continue

    
    try:
        if choice == '1':
            result = num1 + num2
        elif choice == '2':
            result = num1 - num2
        elif choice == '3':
            result = num1 * num2
        elif choice == '4':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2

        print("Result:", result)

    except ZeroDivisionError:
        print("Error: Cannot divide by zero!")


while attempts < 3:
    user_pin = int(input("Enter your PIN: "))

    if user_pin == pin:
        amount = int(input("Enter amount: "))

        if amount <= balance:
            balance -= amount
            print("Withdrawal successful!")
            print("Remaining Balance:", balance)
        else:
            print("Insufficient Balance")
        break 
    else:
        attempts += 1
        print("Incorrect PIN. Attempts left:", 3 - attempts)


if attempts == 3:
    print("Your account is locked due to 3 incorrect attempts.")
