list_of_numbers = [4,	80,	85,	59,	37, 25, 5, 64, 66, 81, 20, 64, 41, 22, 76, 76, 55, 96, 2, 68]


def merge_two_list(list):
    odd = []
    even = []

    for i in list:
        # check if number is even
        if i % 2 == 0:
            even.append(i)
        # check if number is odd
        if i % 2 != 0:
            odd.append(i)
            
    joined_list = [odd] + [even]
    return joined_list


print(merge_two_list(list_of_numbers))