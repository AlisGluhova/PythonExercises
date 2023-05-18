width = int(input())
length = int(input())
volume = width * length

sum_cake = 0
input_line = input()
while input_line != "STOP":
    cake = int(input_line)
    sum_cake += cake
    if sum_cake >= volume:
        break

    input_line = input()

diff = abs(sum_cake - volume)
if sum_cake > volume:
    print(f'No more cake left! You need {diff} pieces more.')
else:
    print(f'{diff} pieces are left.')