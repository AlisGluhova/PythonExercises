number=int(input())
bonus=0
if number<=100:
    bonus=5
elif 100<number<1000:
    bonus=0.2*number
elif number>1000:
    bonus=0.1*number
if number%2==0:
    bonus=bonus+1
elif number%10==5:
    bonus=bonus+2
else:
    bonus=bonus+0
print(bonus)
print(bonus+number)