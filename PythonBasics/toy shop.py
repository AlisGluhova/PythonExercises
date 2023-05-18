price_vacation = float(input())
puzzle = int(input())
doll = int(input())
teddy_bear = int(input())
minions = int(input())
trucks = int(input())
total_amount = puzzle * 2.60 + doll * 3 + teddy_bear * 4.10 + minions * 8.20 + trucks * 2
count = puzzle + doll + teddy_bear + minions + trucks
if count >= 50:
    discount = total_amount * 0.25
    final_amount = total_amount - discount
    rent = 0.1 * final_amount
    profit = final_amount - rent
else:
    rent = 0.1 * total_amount
    profit = total_amount - rent
if profit > price_vacation:
    left = (f"{profit - price_vacation:.2f}")
    print(f'Yes! {left} lv left.')
else:
    needed = (f"{price_vacation - profit:.2f}")
    print(f'Not enough money! {needed} lv needed.')
