budget = int(input())
season = input()
count_people = int(input())
price_boat = 0
if season == 'Spring':
    price_boat = 3000
elif season == 'Summer' or 'Autumn':
    price_boat = 4200
elif season == 'Winter':
    price_boat = 2600

if count_people <= 6:
    price_boat = price_boat * 0.90
elif 7 <= count_people <= 11:
    price_boat = price_boat * 0.85
elif count_people >= 12:
    price_boat = price_boat * 0.75

if count_people % 2 == 0 and season != 'Autumn':
    price_boat = price_boat * 0.95

diff = abs(price_boat - budget)
if price_boat <= budget:
    print(f"Yes! You have {diff:.2f} leva left.")
else:
    print(f"Not enough money! You need {diff:.2f} leva.")
