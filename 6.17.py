time_24hr = input("Enter time (24-hour format): ")

hours, minutes = map(int, time_24hr.split(":"))

if hours >= 12:
    period = "pm"
    if hours > 12:
        hours -= 12  
else:
    period = "am"
    if hours == 0:
        hours = 12  

time_12hr = f"{hours}:{minutes:02d}{period}"

print(f"Time in 12-hour format: {time_12hr}")