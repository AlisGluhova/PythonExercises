book_name = input()
book_counter = 0
input_line = input()
isFound = False
while input_line != "No More Books":
    if book_name == input_line:
        isFound = True
        break

    book_counter += 1
    input_line = input()
if isFound:
    print(f'You checked {book_counter} books and found it.')
else:
    print(f'The book you search is not here!')
    print(f' You checked {book_counter} books.')