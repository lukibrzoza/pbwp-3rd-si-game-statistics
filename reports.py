
# Report functions
def count_games(file_name):
    f = open(file_name, 'r')
    f = f.readlines()
    return len(f)

def decide(file_name, year):
    boolean = False
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        if int(temp[2]) == int(year):
            return True
            break
        else:
            continue

    return boolean

def get_latest(file_name):
    temp_list = []
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        try:
            if int(temp[2]) > int(temp_list[2]):
                temp_list = temp
        except:
            temp_list = temp
            continue

    return str(temp_list[0])

def count_by_genre(file_name, genre):
    count = 0
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        if str(temp[3]) == genre:
            count += 1
        else:
            continue
        
    return count

def get_line_number_by_title(file_name, title):
    count = 1
    f = open(file_name, 'r')
    f = f.readlines()
    for arg in f:
        temp = arg.replace('\t', 'SPLIT')
        temp = temp.replace('\n', '').split('SPLIT')
        if str(temp[0]) != title:
            count += 1
            continue
        else:
            return count
            break


# count_games('game_stat.txt')
# decide('game_stat.txt',1999)
# get_latest('game_stat.txt')
# count_by_genre('game_stat.txt', 'Real-time strategy')
# get_line_number_by_title('game_stat.txt', 'Warcraft III: Reign of Chaos')