import sys
count_movies = int(input())
max_rating_movies_name = ''
max_number = -sys.maxsize
min_rating_movies_name = ''
min_number = sys.maxsize
sum_of_ratings = 0

for i in range(count_movies):
    movies_name = input()
    rating = float(input())

    sum_of_ratings += rating

    if rating > max_number:
        max_number = rating
        max_rating_movies_name = movies_name

    if rating < min_number:
        min_number = rating
        min_rating_movies_name = movies_name

average = sum_of_ratings / count_movies

print(f'{max_rating_movies_name} is with highest rating: {max_number:.1f}')
print(f'{min_rating_movies_name} is with lowest rating: {min_number:.1f}')
print(f'Average rating: {average:.1f}')
