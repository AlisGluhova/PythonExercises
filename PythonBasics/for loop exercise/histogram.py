n = int(input())

p_1=0
p_2=0
p_3=0
p_4=0
p_5=0
for i in range(1, n + 1):
    current_num = int(input())

    if current_num < 200:
        p_1 += 1
    elif current_num <= 399:
        p_2 += 1
    elif current_num <= 599:
        p_3 += 1
    elif current_num <= 799:
        p_4 += 1
    else:
        p_5 += 1

percent_p1 = p_1 / n * 100
print(f"{percent_p1:.2f}%")
percent_p2 = p_2 / n * 100
print(f"{percent_p2:.2f}%")
percent_p3 = p_3 / n * 100
print(f"{percent_p3:.2f}%")
percent_p4 = p_4 / n * 100
print(f"{percent_p4:.2f}%")
percent_p5 = p_5 / n * 100
print(f"{percent_p5:.2f}%")


