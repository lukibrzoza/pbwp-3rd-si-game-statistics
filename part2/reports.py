
# Report functions
def get_most_played(file_name):
    temp_list = []
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        try:
            if float(temp[1]) > float(temp_list[1]):
                temp_list = temp
        except:
            temp_list = temp
            continue
    
    return str(temp_list[0])

def sum_sold(file_name):
    soldcount = 0
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        soldcount += float(temp[1])

    return soldcount

def get_selling_avg(file_name):
    soldcount = 0
    gamecount = 0
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        soldcount += float(temp[1])
        gamecount += 1
    avg = soldcount / gamecount

    return avg

def count_longest_title(file_name):
    temp_list = []
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        try:
            if len(temp[0]) > len(temp_list[0]):
                temp_list = temp
        except:
            temp_list = temp
            continue

    return str(len(temp_list[0]))

def get_date_avg(file_name):
    yearcount = 0
    gamecount = 0
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        yearcount += int(temp[2])
        gamecount += 1
    avg = yearcount / gamecount

    return round(avg + 0.5)

def get_game(file_name, title):
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        if str(temp[0]) != title:
            continue
        else:
            return temp
            break

# get_most_played('game_stat.txt')
# sum_sold('game_stat.txt')
# get_selling_avg('game_stat.txt')
# count_longest_title('game_stat.txt')
# get_date_avg('game_stat.txt')
# get_game('game_stat.txt', 'Terraria')