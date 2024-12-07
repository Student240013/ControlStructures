
driving_mode = input('Enter driving mode (A/M/E): ').strip().upper() 
distance = int(input('Enter distance in km: '))

if driving_mode == 'A':
    fuel_consumption = 7 
elif driving_mode == 'M':
    fuel_consumption = 9 
elif driving_mode == 'E':
    fuel_consumption = 6 
else:
    fuel_consumption = None 

if fuel_consumption is not None:
    total_consumption = (fuel_consumption * distance) / 100
    print(f'Total fuel consumption over a distance of {distance} km in driving mode {driving_mode} is {total_consumption:.1f} liters')
else:
    print('Invalid driving mode entered.')