hours_parked = int(input("Enter the number of hours parked: "))

if hours_parked <= 2:
    fee = 5
elif 3 <= hours_parked <= 6:
    fee = 15
else:
    fee = 20

print(f"The parking fee is: {fee} PLN")