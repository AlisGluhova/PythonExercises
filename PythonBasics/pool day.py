import math

people_count = int(input())
tax_enter = float(input())
price_sunbed = float(input())
price_umbrella = float(input())

entrance = tax_enter * people_count
umbrella = math.ceil((people_count / 2)) * price_umbrella
sunbed = math.ceil((people_count * 0.75)) * price_sunbed

total_sum = entrance + umbrella + sunbed

print(f"{total_sum:.2f} lv.")