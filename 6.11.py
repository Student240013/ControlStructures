current_price = float(input("Enter the current product price: "))
previous_price = float(input("Enter the previous product price: "))

price_reduction_percentage = ((previous_price - current_price) / previous_price) * 100

if price_reduction_percentage >= 10:
    print("Buy the product!!")
    print(f"Product price reduced by {int(price_reduction_percentage)}%")
else:
    print("Price reduction is less than 10%, no recommendation to buy.")