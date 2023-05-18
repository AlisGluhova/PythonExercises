budget = float(input())
N = int(input())
M = int(input())
P = int(input())
amount_N = 250 * N
amount_M = amount_N * 0.35 * M
amount_P = amount_N * 0.10 * P
final_amount = amount_P + amount_M + amount_N
if N > M:
    final_amount = final_amount - 15 / 100 * final_amount
    if final_amount <= budget:
        money_left = (f"{budget - final_amount:.2f}")
        print(f'You have {money_left} leva left!')
    else:
        money_needed = (f"{final_amount - budget:.2f}")
        print(f'Not enough money! You need {money_needed} leva more!')
else:
    if final_amount <= budget:
        money_left = (f"{budget - final_amount:.2f}")
        print(f'You have {money_left} leva left!')
    else:
        money_needed = (f"{final_amount - budget:.2f}")
        print(f'Not enough money! You need {money_needed} leva more!')