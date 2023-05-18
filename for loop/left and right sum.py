number_of_lines = int(input()) * 2
left_sum = 0
right_sum = 0

for num in range(1, number_of_lines + 1):
    current_num = int(input())
    if 1 <= num <= number_of_lines / 2:
        left_sum += current_num
    else:
        right_sum += current_num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    diff = abs(left_sum - right_sum)
    print(f"No, diff = {diff}")