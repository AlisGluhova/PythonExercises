number_poor_grade = int(input())

flag = False
last_problem = ""
sum_grade = 0
counter_problems = 0
current_count_poor = 0
input_line = input()
while input_line != "Enough":
    problem_name = input_line
    current_grade = int(input())
    if current_grade <= 4:
        current_count_poor += 1

    if current_count_poor >= number_poor_grade:
        flag = True
        break

    sum_grade += current_grade
    counter_problems += 1

    last_problem = problem_name
    input_line = input()
if flag:
    print(f'You need a break, {current_count_poor} poor grades.')
else:
    average_grades = sum_grade / counter_problems
    print(f"Average score: {average_grades:.2f}")
    print(f'Number of problems: {counter_problems}')
    print(f'Last problem: {last_problem}')
