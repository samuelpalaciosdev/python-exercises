my_list = [2323,4344,2325,324413,21234,24531,2123,42234,544,456,345,42,5445,23,5656,423]

def find_average(list):
    sum = 0
    last_index = len(my_list)
    for num in list:
        sum = sum + num
    average = sum / last_index
    return average

print(find_average(my_list))

