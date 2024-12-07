decimal_number = int(input("Enter decimal number: "))

original_number = decimal_number

binary_digits = []

while decimal_number > 0:
    remainder = decimal_number % 2  
    binary_digits.append(str(remainder))  
    decimal_number = decimal_number // 2  

if not binary_digits:
    binary_digits.append('0')

binary_digits.reverse()
binary_number = ''.join(binary_digits)

print(f"{original_number}(10) = {binary_number}(2)")