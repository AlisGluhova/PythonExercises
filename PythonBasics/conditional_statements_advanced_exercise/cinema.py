type_projection = input()
lines = int(input())
columns = int(input())
income = 0
cinema_capacity=lines*columns
if type_projection=='Premiere':
    income=cinema_capacity*12.00
    print(f'{income:.2f} leva')
elif type_projection=='Normal':
    income=cinema_capacity*7.50
    print(f'{income:.2f} leva')
elif type_projection=='Discount':
    income=cinema_capacity*5.00
    print(f'{income:.2f} leva')