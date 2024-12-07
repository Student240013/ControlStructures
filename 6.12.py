def calculate_total_price(num_products, product_price):
    if num_products > 2:
        discount = 0.25 
    else:
        discount = 0 
    
    total_price = num_products * product_price
    
    total_price_after_discount = total_price * (1 - discount)
    
    return total_price_after_discount

num_products = int(input("Number of products purchased: "))
product_price = float(input("Product price: "))

amount_to_pay = calculate_total_price(num_products, product_price)

print(f"Amount to pay: {amount_to_pay:.2f}")