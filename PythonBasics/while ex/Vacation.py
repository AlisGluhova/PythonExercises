needed_money = float(input())
init_money = float(input())

count_spend_days = 0
count_total_days = 0
total_sum = init_money
while total_sum < needed_money:
    if count_spend_days == 5:
        break
    action = input()
    amount = float(input())

    count_total_days += 1

    if action == "spend":
        total_sum -= amount
        count_spend_days += 1
        if total_sum < 0:
            total_sum = 0
    elif action == "save":
        count_spend_days = 0
        total_sum += amount


if count_spend_days == 5:
    print(f"You can't save the money.")
    print(f'{count_total_days}')
else:
    print(f'You saved the money for {count_total_days} days.')
