
# Export functions
import os
from reports import *

def export_reports():
    filename = input('Enter file name: ')
    try:
        f = open('export.txt', 'w')
        f.write(str(get_most_played(filename)) + '\n' + str(sum_sold(filename)) + '\n' + str(get_selling_avg(filename)) + '\n' + str(count_longest_title(filename)) + '\n' + str(get_date_avg(filename)) + '\n' + str(get_game(filename, input('Enter title '))))
        f.close()
    except FileNotFoundError:
        os.mkdir('export.txt')



export_reports()