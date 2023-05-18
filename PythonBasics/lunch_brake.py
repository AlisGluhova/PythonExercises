from math import ceil

series=str(input())
episode_duration=int(input())
brake_duration=int(input())

lunch_time=brake_duration/8
relax_time=brake_duration/4
time=brake_duration-lunch_time-relax_time
diff=abs(time-episode_duration)
rounded_diff=ceil(diff)
if episode_duration<=time:
    print(f'You have enough time to watch {series} and left with {rounded_diff} minutes free time.')
else:
    print(f"You don't have enough time to watch {series}, you need {rounded_diff} more minutes.")