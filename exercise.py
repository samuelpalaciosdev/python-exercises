def lyrics_generator(list):
    store = ''
    for i in range(len(list)):
        if list[i] == 0:
            store += 'Boom '
        elif i > 1 and list[i] == 1 and list[i - 1] == 1 and list[i - 2] == 1:
            store += 'Drop the base !!!Break the base!!! '
        else:
            store += 'Drop the base '
    return store
        


# Your code go above, nothing to change after this line:
print(lyrics_generator([0,0,1,1,0,0,0]))
print(lyrics_generator([0,0,1,1,1,0,0,0]))
print(lyrics_generator([0,0,0]))
print(lyrics_generator([1,0,1]))
print(lyrics_generator([1,1,1]))
