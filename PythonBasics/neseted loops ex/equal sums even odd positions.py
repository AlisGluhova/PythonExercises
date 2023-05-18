first_number = int(input())
second_number = int(input())
for number in range(first_number, second_number + 1):
    hundred_thousands = number // 100000
    ten_thousands = (number // 10000) % 10
    thousands = (number // 1000) % 10
    hundreds = (number // 100) % 10
    tens = (number // 10) % 10
    units = number % 10

    sum_even = ten_thousands + hundreds + units
    sum_odd = hundred_thousands + thousands + tens
    if sum_odd == sum_even:
        print(number, end=" ")
