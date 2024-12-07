basic_salary = 5000
total_salary = 0
bonus = 0.15
is_bonus = input('Does the employee receive a bonus? (Y/N): ') == 'Y'

if is_bonus:
    bonus_amount = basic_salary * bonus
    total_salary = basic_salary + bonus_amount
else:
    total_salary = basic_salary

print(f'Basic salary: {basic_salary} PLN')
print(f'Bonus included? {"Yes" if is_bonus else "No"}')
print(f'Total salary: {total_salary} PLN')