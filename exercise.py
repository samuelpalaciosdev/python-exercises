par = "Hello World"

counts = {}

def count_chars(str):
    # remove white spaces from string and transform it to lowercase
    str = str.replace(' ', '').lower()
    global counts
    # for each letter in the string
    for letter in str:
        # if the letter is not present on the counts dict
        if letter not in counts:
            # default value to 0
            counts[letter] = 0
        # for each ocurrence of a letter, add one to its counter
        counts[letter] += 1
    return counts

print(count_chars(par)) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}
print(counts) # {'h': 1, 'e': 1, 'l': 3, 'o': 2, 'w': 1, 'r': 1, 'd': 1}