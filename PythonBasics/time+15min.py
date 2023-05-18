hours=int(input())
minutes=int(input())
if 0<=hours<=23:
    if 0<=minutes<=59:
        result=minutes+15
        if result>=60:
            final_time=hours+1
            final_minutes=result-60
            if final_time==24:
                final_time=0
            if final_minutes < 10:
                print(f'{final_time}:0{final_minutes}')
            else:
                print(f'{final_time}:{final_minutes}')
        else:
            if result < 10:
                print(f'{hours}:0{result}')
            else:
                print(f'{hours}:{result}')

