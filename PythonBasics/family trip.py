budget = float(input())
nights = int(input())
price_per_night = float(input())
extra_expenses = float(input())

amount_for_nights = nights * price_per_night
if nights > 7:
    discount=price_per_night*0.95
    amount_for_nights=nights*discount

amount_extra_expenses=extra_expenses/100*budget

final_amount=amount_extra_expenses+amount_for_nights

diff=abs(final_amount-budget)
if final_amount <= budget:
    print(f'Ivanovi will be left with {diff:.2f} leva after vacation."')
else:
    print(f'{diff:.2f} leva needed.')
