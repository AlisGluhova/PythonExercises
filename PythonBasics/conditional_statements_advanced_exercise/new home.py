type_flower = input()
count = int(input())
budget = int(input())
final_amount = 0
if type_flower == "Roses":
    final_amount = count * 5.00
    if count > 80:
        final_amount = final_amount * 0.90
elif type_flower == "Dahlias":
    final_amount = count * 3.80
    if count > 90:
        final_amount = final_amount * 0.85
elif type_flower == "Tulips":
    final_amount = count * 2.80
    if count > 80:
        final_amount = final_amount * 0.8
elif type_flower == "Narcissus":
    final_amount = count * 3.00
    if count < 120:
        final_amount = final_amount * 1.15
elif type_flower == "Gladiolus":
    final_amount = count * 2.50
    if count < 80:
        final_amount = final_amount * 1.20

diff = abs(final_amount - budget)
if final_amount <= budget:
    print(f'Hey, you have a great garden with {count} {type_flower} and {diff:.2f} leva left.')
else:
    print(f'Not enough money, you need {diff:.2f} leva more.')
