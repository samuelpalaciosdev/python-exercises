my_list = [42, True, "towel", [2,1], 'hello', 34.4, {"name": "juan"}]

new_list = []
last_index = len(my_list)

for i in range(0, last_index, 1):
    if type(my_list[i]) == list or type(my_list[i]) == dict:
        new_list.append(my_list[i])
print(new_list)