myNumbers = [23,234,345,4356234,243,43,56,2]

def multiplied_by_3(num):
    return num * 3

new_list = list(map(multiplied_by_3, myNumbers))


print(new_list) # [69, 702, 1035, 13068702, 729, 129, 168, 6]