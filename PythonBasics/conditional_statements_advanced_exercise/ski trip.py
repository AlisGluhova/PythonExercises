days = int(input())
room = input()
grade = input()
price = 0
if room == "room for one person":
    price = 18
    final_amount = (days - 1) * price
    if grade == "positive":
        final_amount = final_amount * 1.25
    else:
        final_amount = final_amount * 0.90
    print(f'{final_amount:.2f}')
elif room == "apartment":
    price = 25
    final_amount = (days - 1) * price
    if days-1 < 10:
        final_amount = final_amount * 0.70
    elif 10 <= days-1 <= 15:
        final_amount = final_amount * 0.65
    else:
        final_amount = final_amount * 0.50
    if grade == "positive":
        final_amount = final_amount * 1.25
    else:
        final_amount = final_amount * 0.90
    print(f'{final_amount:.2f}')
elif room == "president apartment":
    price = 35
    final_amount = (days - 1) * price
    if days-1 < 10:
        final_amount = final_amount * 0.90
    elif 10 <= days-1 <= 15:
        final_amount = final_amount * 0.85
    else:
        final_amount = final_amount * 0.80
    if grade == "positive":
        final_amount = final_amount * 1.25
    else:
        final_amount = final_amount * 0.90
    print(f'{final_amount:.2f}')
