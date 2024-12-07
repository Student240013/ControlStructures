balance = 1000  
pin = '1111'  

def check_pin():
    """Verify the user's PIN before allowing access."""
    attempts = 3
    while attempts > 0:
        entered_pin = input("Enter your 4-digit PIN: ")
        if entered_pin == pin:
            return True
        else:
            attempts -= 1
            print(f"Incorrect PIN. You have {attempts} attempt(s) remaining.")
    print("Too many incorrect attempts. Exiting...")
    return False

def change_pin():
    """Allow the user to change their PIN."""
    global pin
    current_pin = input("Enter your current PIN: ")
    if current_pin != pin:
        print("Incorrect current PIN. PIN change aborted.")
        return
    new_pin = input("Enter your new 4-digit PIN: ")
    if len(new_pin) == 4 and new_pin.isdigit():
        confirm_pin = input("Re-enter your new PIN to confirm: ")
        if new_pin == confirm_pin:
            pin = new_pin
            print("Your PIN has been successfully changed.")
        else:
            print("PINs do not match. PIN change aborted.")
    else:
        print("Invalid PIN. It must be exactly 4 digits.")

if check_pin():
    while True:
        print()
        print("ATM Menu:")
        print("1. Check balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")
        print()

        if choice == '1':
            print(f"Your current balance is: €{balance}")
        elif choice == '2':
            amount = float(input("Enter the amount to deposit: "))
            balance += amount
            print(f"€{amount} has been deposited. New balance: €{balance}")
        elif choice == '3':
            amount = float(input("Enter the amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"€{amount} has been withdrawn. New balance: €{balance}")
            else:
                print("Insufficient balance.")
        elif choice == '4':
            change_pin()
        elif choice == '5':
            print("Exiting... Thank you for using the ATM!")
            break 
        else:
            print("Invalid option. Please try again.")