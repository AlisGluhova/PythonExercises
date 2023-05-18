jury = int(input())

all_grades = 0
counter_all = 0

project = input()
while project != "Finish":
    sum_grades = 0
    for jury in range(1, jury + 1):
        current_grade = float(input())
        counter_all += 1
        sum_grades += current_grade
        all_grades += current_grade

    average_grades = sum_grades / jury
    print(f'{project} - {average_grades:.2f}')

    project = input()

final_ave = all_grades / counter_all
print(f"Student's final assessment is {final_ave:.2f}")
