dog_age_human_years = int(input("Enter the dog's age in human years: "))

if dog_age_human_years <= 2:
    dog_age_dog_years = dog_age_human_years * 10.5
else:
    dog_age_dog_years = 2 * 10.5 + (dog_age_human_years - 2) * 4

print(f"The dog's age in dog's years is {int(dog_age_dog_years)} years.")