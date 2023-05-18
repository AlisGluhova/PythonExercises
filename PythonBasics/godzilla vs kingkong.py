budget=float(input())
actors=int(input())
price_per_actor_costume=float(input())
decoration=budget*0.1
price_costumes=price_per_actor_costume*actors
if actors>150:
    price_costumes=price_costumes-price_costumes*0.1
final_amount=decoration+price_costumes
if final_amount>budget:
    needed_money=final_amount-budget
    print(f'Not enough money!')
    print(f'Wingard needs {needed_money:.2f} leva more.')
else:
    money_left=budget-final_amount
    print(f'Action!')
    print(f'Wingard starts filming with {money_left:.2f} leva left.')