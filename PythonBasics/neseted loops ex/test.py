movie = input()
seats = int(input())
student_count = 0
kid_count = 0
standard_count = 0
count_tickets = 0
while movie != "Finish":
    ticket = input()
    count_tickets += 1

    if ticket == "student":
        student_count += 1
    elif ticket == "kid":
        kid_count += 1
    elif ticket == "standard":
        standard_count += 1

    print(count_tickets)

    ticket = input()
