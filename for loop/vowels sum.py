text=input()
total_sum=0
for i in text:
    if i == "a":
        total_sum += 1
    elif i == "e":
        total_sum += 2
    elif i == "i":
        total_sum += 3
    elif i == "o":
        total_sum += 4
    elif i == "u":
        total_sum += 5
print(total_sum)