correct_pin = "0805"

attempts = 3

for i in range(attempts):
    pin = input("Enter the PIN code: ")
    
    if pin == correct_pin:
        print("Access granted.")
        break
    else:
        print("Incorrect...")
    
    if i == attempts - 1:
        print("Sorry, your payment card has been blocked.")