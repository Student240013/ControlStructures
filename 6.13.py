speed_limit_min = 40
speed_limit_max = 140

car_speed = int(input("Enter car speed: "))

if car_speed < speed_limit_min or car_speed > speed_limit_max:
    print("Warning: invalid car speed!!")
else:
    print("Car speed is within the valid range.")