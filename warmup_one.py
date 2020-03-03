def sleep_in(weekday,vacation):
    if not weekday or vacation:
        return True
    else:
        return False
    

def monkey_trouble(a_smile,b_smile):
    if a_smile == b_smile:
        return True
    else:
        return False
    

def sum_double(first_num,second_num):
    sum = first_num + second_num
    if first_num == second_num:
        return sum*2
    return sum


def find_life():
    life = input()
    while(life != 42):
        print(life)
        find_life()
