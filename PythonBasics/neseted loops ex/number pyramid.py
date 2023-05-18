number = int(input())
current_number = 1
current_number_bigger_than_number = False

for row in range(1, number + 1):
    for col in range(1, row + 1):

        if current_number > number:
            current_number_bigger_than_number = True
            break
        print(f'{current_number}', end=" ")
        current_number += 1
    if current_number_bigger_than_number > number:
        break
    print()
