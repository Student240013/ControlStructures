total_tasks = 20
tasks_ok = int(input('Enter the number of correctly completed tasks: '))
test_passed = False

if tasks_ok >= total_tasks * 0.5:  # Check if tasks_ok is at least 50% of total_tasks
    test_passed = True

if test_passed:
    print('Congratulations! You passed the test.')
else:
    print('Unfortunately, you failed the test.')