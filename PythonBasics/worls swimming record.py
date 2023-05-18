import math
record = float(input())
distance = float(input())
seconds_meter = float(input())
if record>0:
    if distance>0:
        if seconds_meter>0:
            time = float(f'{distance * seconds_meter:.2f}')
            water = math.floor(distance / 15.00)
            seconds_water = float(f'{water * 12.50:.2f}')
            whole_time = float(f'{time + seconds_water:.2f}')
            if whole_time >= record:
                needed_time = whole_time - record
                print(f'No, he failed! He was {needed_time:.2f} seconds slower.')
            else:
                print(f'Yes, he succeeded! The new world record is {whole_time:.2f} seconds.')
