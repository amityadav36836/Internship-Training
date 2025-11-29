balance = 5000
pin = 1234
attempts = 0
locked = False

transaction_history = []  
last_transaction = None
daily_withdrawn = 0
DAILY_LIMIT = 20000      

def save_receipt(transaction, balance_after):
    """Save last transaction receipt to a text file."""
    with open("receipt.txt", "w") as f:
        f.write("---- ATM RECEIPT ----\n")
        f.write(f"Transaction: {transaction}\n")
        f.write(f"Available Balance: {balance_after}\n")
        f.write("---------------------\n")
    print("Receipt saved to receipt.txt\n")


while attempts < 3 and not locked:
    try:
        user_pin = int(input("Enter your PIN: ").strip())
    except ValueError:
        print("PIN must be numbers only.\n")
        continue

    if user_pin == pin:
        print("\nLogin Successful!\n")

       
        while True:
            print("----- ATM Menu -----")
            print("1. Withdraw")
            print("2. Deposit")
            print("3. Check Balance")
            print("4. Change PIN")
            print("5. Print/Save Receipt (last transaction)")
            print("6. Transaction History")
            print("7. Exit")
            choice = input("Enter choice (1-7): ").strip()

            if choice == "1":
                try:
                    amount = int(input("Enter amount to withdraw: ").strip())
                except ValueError:
                    print("Amount must be a number.\n")
                    continue

                if amount <= 0:
                    print("Enter a positive amount.\n")
                    continue

                if daily_withdrawn + amount > DAILY_LIMIT:
                    print(f"Daily limit exceeded. You can withdraw up to {DAILY_LIMIT - daily_withdrawn} more today.\n")
                    continue

                if amount > balance:
                    print("Insufficient balance.\n")
                    continue

                balance -= amount
                daily_withdrawn += amount
                last_transaction = f"Withdraw: {amount}"
                transaction_history.append(("Withdraw", amount))
                print("Withdrawal successful!")
                print("Remaining balance:", balance, "\n")

            elif choice == "2":
               
                try:
                    amount = int(input("Enter amount to deposit: ").strip())
                except ValueError:
                    print("Amount must be a number.\n")
                    continue

                if amount <= 0:
                    print("Enter a positive amount.\n")
                    continue

                balance += amount
                last_transaction = f"Deposit: {amount}"
                transaction_history.append(("Deposit", amount))
                print("Deposit successful!")
                print("New balance:", balance, "\n")

            elif choice == "3":
               
                print("Your current balance is:", balance, "\n")

            elif choice == "4":
                
                try:
                    old = int(input("Enter current PIN: ").strip())
                except ValueError:
                    print("PIN must be numbers only.\n")
                    continue

                if old != pin:
                    print("Current PIN is incorrect.\n")
                    continue

                try:
                    new = int(input("Enter new PIN (4 digits recommended): ").strip())
                    confirm = int(input("Confirm new PIN: ").strip())
                except ValueError:
                    print("PIN must be numbers only.\n")
                    continue

                if new != confirm:
                    print("PINs do not match. Try again.\n")
                    continue

                pin = new
                print("PIN changed successfully!\n")

            elif choice == "5":
               
                if last_transaction:
                    print("----- Receipt -----")
                    print("Last transaction:", last_transaction)
                    print("Available balance:", balance)
                    print("-------------------\n")

                    save = input("Do you want to save this receipt to file? (y/n): ").strip().lower()
                    if save == "y":
                        save_receipt(last_transaction, balance)
                else:
                    print("No transactions yet.\n")

            elif choice == "6":
              
                if transaction_history:
                    print("---- Transaction History ----")
                    for i, (t_type, amt) in enumerate(transaction_history, start=1):
                        print(f"{i}. {t_type} - {amt}")
                    print("-----------------------------\n")
                else:
                    print("No transactions recorded yet.\n")

            elif choice == "7":
                print("Thank you! Exiting...\n")
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 7.\n")

        break  

    else:
        attempts += 1
        print("\nIncorrect PIN")
        if attempts == 3:
            locked = True
            print("Your account is LOCKED after 3 wrong attempts.\n")
        else:
            print(f"You have {3 - attempts} attempt(s) left.\n")