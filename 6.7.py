age = int(input("Enter your age: "))

if age < 13:
    print("You are a Child.")
elif 13 <= age <= 19:
    print("You are a Teen.")
elif 20 <= age <= 64:
    print("You are an Adult.")
else:
    print("You are a Senior.")