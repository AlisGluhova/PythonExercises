month = str(input())
days = int(input())

if month == 'May' or month == 'October':
    studio = 50
    apartment = 65
    price_studio = studio * days
    price_apartment = apartment * days
    if 7 < days < 14:
        final_price_studio = price_studio - (price_studio * (5/100))
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {final_price_studio:.2f} lv.')
    elif days >= 14:
        final_price_studio = price_studio - (price_studio * (30/100))
        final_price_apart = price_apartment - (price_apartment * (10/100))
        print(f'Apartment: {final_price_apart:.2f} lv.')
        print(f'Studio: {final_price_studio:.2f} lv.')
    else:
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')


elif month == 'June' or month == 'September':
    studio = 75.20
    apartment = 68.70
    price_studio = studio * days
    price_apartment = apartment * days
    if days > 14:
        final_price_studio = price_studio - (price_studio * (20 / 100))
        final_price_apart = price_apartment - (price_apartment * (10 / 100))
        print(f'Apartment: {final_price_apart:.2f} lv.')
        print(f'Studio: {final_price_studio:.2f} lv.')
    else:
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')

elif month == 'July' or month == 'August':
    studio = 76
    apartment = 77
    price_studio = studio * days
    price_apartment = apartment * days
    if 7 <= days < 14:
        final_price_studio = price_studio - (price_studio * (5/100))
        final_price_apart = price_apartment
        print(f'Apartment: {final_price_apart:.2f} lv.')
        print(f'Studio: {final_price_studio:.2f} lv.')
    elif days > 14:
        final_price_studio = price_studio
        final_price_apart = price_apartment - (price_apartment * (10/100))
        print(f'Apartment: {final_price_apart:.2f} lv.')
        print(f'Studio: {final_price_studio:.2f} lv.')
    else:
        print(f'Apartment: {price_apartment:.2f} lv.')
        print(f'Studio: {price_studio:.2f} lv.')
