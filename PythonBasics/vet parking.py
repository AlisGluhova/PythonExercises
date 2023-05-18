count_days = int(input())
count_hours = int(input())
total_cost = 0

for days in range(1, count_days + 1):
    current_costs = 0
    for hour in range(1, count_hours + 1):
        if days % 2 == 0 and hour % 2 != 0:
            current_costs += 2.5
            total_cost += 2.5
        elif days % 2 != 0 and hour % 2 == 0:
            current_costs += 1.25
            total_cost += 1.25
        else:
            current_costs += 1
            total_cost += 1

    print(f'Day: {days} - {current_costs:.2f} leva')
print(f'Total: {total_cost:.2f} leva')