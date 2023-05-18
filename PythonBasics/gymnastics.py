country = input()
object = input()
difficulty = 0
performance = 0

if country == "Russia":
    if object == "ribbon":
        difficulty = 9.100
        performance = 9.400
    elif object == "hoop":
        difficulty = 9.300
        performance = 9.800
    elif object == "rope":
        difficulty = 9.600
        performance = 9.000
elif country == "Bulgaria":
    if object == "ribbon":
        difficulty = 9.600
        performance = 9.400
    elif object == "hoop":
        difficulty = 9.550
        performance = 9.750
    elif object == "rope":
        difficulty = 9.500
        performance = 9.400
if country == "Italy":
    if object == "ribbon":
        difficulty = 9.200
        performance = 9.500
    elif object == "hoop":
        difficulty = 9.450
        performance = 9.350
    elif object == "rope":
        difficulty = 9.700
        performance = 9.150

points = difficulty + performance
diff = 20 - points
percent = (diff / 20) * 100

print(f'The team of {country} get {points:.3f} on {object}.')
print(f'{percent:.2f}%')
