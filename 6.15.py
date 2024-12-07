ean = input("Enter EAN-13 article number: ")

if len(ean) == 13 and ean.isdigit():
    print("Article number is correct")
    
    if ean[:3] == "590":
        print("Article manufactured in Poland")
else:
    print("Invalid article number")