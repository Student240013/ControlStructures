washing_times = {
    "jacket": 40,
    "underwear": 70,
    "shoes": 20
}

rinse_time = 15
spin_time = 9

washing_product = input('Select washing program: (j)acket, (u)nderwear, (s)hoes: ').lower()
rinse = input('Extra rinse? (y/n): ').lower() == 'y'
spin = input('Extra spin? (y/n): ').lower() == 'y'

if washing_product == 'jacket':
    total_washing_time = washing_times["jacket"]
elif washing_product == 'underwear':
    total_washing_time = washing_times["underwear"]
elif washing_product == 'shoes':
    total_washing_time = washing_times["shoes"]
else:
    print("Invalid washing program selected.")
    exit()

if rinse:
    total_washing_time += rinse_time
if spin:
    total_washing_time += spin_time

print(f"Total washing time: {total_washing_time} minutes")