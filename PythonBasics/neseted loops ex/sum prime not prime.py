input_line = input()

sum_prime = 0
sum_non_prime = 0
while input_line != 'stop':
    current_number = int(input_line)

    if current_number < 0:
        print(f'Number is negative.')
        input_line = input()
        continue

    count = 0
    for n in range(1, current_number + 1):
        if current_number % n == 0:
            count += 1
    if count == 2:
        sum_prime += current_number
    else:
        sum_non_prime += current_number
    input_line = input()

print(f'Sum of all prime numbers is: {sum_prime}')
print(f'Sum of all non prime numbers is: {sum_non_prime}')
