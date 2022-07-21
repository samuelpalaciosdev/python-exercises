i = 20

while i >= 0:
    # check if number is 0
    if i == 0:
        print('LIFTOFF')
    # check if number is multiple of 5
    elif i %5 == 0:
        print(f'{i}!')
    else:
        print(i)
    # decrement on each iteration
    i -= 1
    