n = int(input())

for thousand in range(1, 10):
    for hundred in range(1, 10):
        for ten in range(1, 10):
            for unit in range(1, 10):
                if n % thousand == 0 and n % hundred == 0 and n % ten == 0 and n % unit == 0:
                    print(f'{thousand}{hundred}{ten}{unit}', end=' ')
