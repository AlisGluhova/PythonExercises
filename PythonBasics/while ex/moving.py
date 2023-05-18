width = int(input())
length = int(input())
height = int(input())

sum_space = width * length * height
boxes_sum = 0
input_lines = input()
while input_lines != "Done":
    boxes = int(input_lines)
    boxes_sum += boxes

    if boxes_sum >= sum_space:
        break

    input_lines = input()

diff = abs(boxes_sum - sum_space)
if boxes_sum > sum_space:
    print(f'No more free space! You need {diff} Cubic meters more.')
else:
    print(f'{diff} Cubic meters left.')
