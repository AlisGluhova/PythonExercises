import math

count_tournaments = int(input())
init_points = int(input())

percent_won=0
count_w = 0
total_points = init_points
for i in range(1, count_tournaments + 1):
    tournament_stage = input()

    if tournament_stage == "W":
        total_points += 2000
        count_w += 1
        percent_won = (count_w / count_tournaments) * 100
    elif tournament_stage == "F":
        total_points += 1200
    elif tournament_stage == "SF":
        total_points += 720

average_points = math.floor((total_points - init_points) / count_tournaments)
print(f'Final points: {total_points}')
print(f'Average points: {average_points}')
print(f'{percent_won:.2f}%')



