
# Printing functions
from reports import *
while True:
    menu_select = input('Please select which question do you want to be answered:\n\
    1. What is the title of the most played game?\n\
    2. How many copies have been sold total?\n\
    3. What is the average selling?\n\
    4. How many characters long is the longest title?\n\
    5. What is the average of the release dates?\n\
    6. What properties has a game?\n')
    
    if menu_select == '1':
        try:
            print('Answer: ' + str(get_most_played(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue
    
    elif menu_select == '2':
        try:
            print('Answer: ' + str(sum_sold(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '3':
        try:
            print('Answer: ' + str(get_selling_avg(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '4':
        try:
            print('Answer: ' + str(count_longest_title(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '5':
        try:
            print('Answer: ' + str(get_date_avg(input('Please enter the name of the file: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    elif menu_select == '6':
        try:
            print('Answer: ' + str(get_game(input('Please enter the name of the file: '), input('Please enter game title: '))) + '\n')
        except FileNotFoundError:
            print('\nPlease enter a correct file name.\n')
            continue

    else:
        print('\nPlease enter a valid number.\n')
        continue