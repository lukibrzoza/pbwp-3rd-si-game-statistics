
# Export functions
import os
from reports import *

def export_reports():
    filename = input('Enter file name: ')
    try:
        f = open('export.txt', 'w')
        f.write(str(count_games(filename)) + '\n' + str(decide(filename, input('Enter year:'))) + '\n' + str(get_latest(filename)) + '\n' + str(count_by_genre(filename, input('Enter genre: '))) + '\n' + str(get_line_number_by_title(filename, input('Enter title: '))))
        f.close()
    except FileNotFoundError:
        os.mkdir('export.txt')



export_reports()