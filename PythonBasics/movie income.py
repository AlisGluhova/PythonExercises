movie_name = input()
days = int(input())
tickets = int(input())
price_for_ticket = float(input())
percent_for_cinema = float(input())

amount_for_tickets = tickets * price_for_ticket
whole_amount = days * amount_for_tickets

amount_for_cinema=percent_for_cinema/100*whole_amount

final_income= whole_amount-amount_for_cinema
print(f'The profit from the movie {movie_name} is {final_income:.2f} lv.')