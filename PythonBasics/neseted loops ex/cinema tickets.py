movie = input()
seats = int(input())
student_count = 0
kid_count = 0
standard_count = 0
count_tickets = 0
input_line = input()

while input_line != "Finish":
    ticket = input_line
    count_tickets += 1

    if ticket == "student":
        student_count += 1
    elif ticket == "kid":
        kid_count += 1
    elif ticket == "standard":
        standard_count += 1

    percent_full = count_tickets / seats * 100
    if count_tickets == seats or ticket == "End":
        print(f'{movie} - {percent_full:.2f}% full.')

    input_line = input()
print(f'Total tickets: {count_tickets}')
percent_student = student_count / count_tickets * 100
print(f'{percent_student:.2f}% student tickets.')
percent_standard = standard_count / count_tickets * 100
print(f'{percent_standard:.2f}% standard tickets.')
percent_kid = kid_count / count_tickets * 100
print(f'{percent_kid:.2f}% kids tickets.')