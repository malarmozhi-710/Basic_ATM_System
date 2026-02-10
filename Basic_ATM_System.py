pin = "1234"
balance = 5000

print("===== WELCOME TO ATM =====")

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    print("\nPIN verified successfully!")

    while True:
        print("\n--- ATM MENU ---")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            print(f"Your current balance is: ₹{balance}")

        elif choice == "2":
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
            else:
                print("Invalid deposit amount.")

        elif choice == "3":
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Invalid withdrawal amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance -= amount
                print(f"₹{amount} withdrawn successfully.")

        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

else:
    print("Incorrect PIN. Access denied.")