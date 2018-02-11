
# Printing functions
from reports import *
while True:
    menu_select = input('Please select which question do you want to be answered:\n\
    1. How many games are in the file?\n\
    2. Is there a game from a given year?\n\
    3. Which was the latest game?\n\
    4. How many games do we have by genre?\n\
    5. What is the line number of the given game (by title)?\n')
    
    if menu_select == '1':
        try:
            print('Answer: ' + str(count_games(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue
    
    elif menu_select == '2':
        try:
            print('Answer: ' + str(decide(input('Please enter the name of the file: '), input('Please enter a year: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '3':
        try:
            print('Answer: ' + str(get_latest(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '4':
        try:
            print('Answer: ' + str(count_by_genre(input('Please enter the name of the file: ')), input('Please enter a genre: ')) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '5':
        try:
            print('Answer: ' + str(get_line_number_by_title(input('Please enter the name of the file: ')), input('Please enter game title: ')) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    else:
        print('\nPlease enter a valid number.\n')
        continue