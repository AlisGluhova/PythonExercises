age = int(input())
washer_price = float(input())
price_per_toy = int(input())
brother_count=0
total_sum=0
money = 10
toy = 0
for i in range(1, age + 1):
    if i % 2 != 0:
        toy += 1
    else:
        brother_count += 1
        total_sum += money
        money += 10
sum_toys = toy * price_per_toy
total_amount = (total_sum + sum_toys) - brother_count

diff=0
diff=abs(washer_price-total_amount)
if total_amount >= washer_price:
    print(f'Yes! {diff:.2f}')
else:
    print(f'No! {diff:.2f}')