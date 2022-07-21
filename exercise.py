theBools = [0,1,0,0,1,1,1,0,0,1,0,1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1]

#Your code go here:

def yes_or_no(num):
    if num == 1:
        return 'wiki'
    elif num == 0:
        return 'woko'

result = list(map(yes_or_no, theBools))
print(result)

