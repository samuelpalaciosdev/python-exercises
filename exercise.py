all_names = ["Romario","Boby","Roosevelt","Emiliy", "Michael", "Greta", "Patricia", "Danzalee"]

def names_check(name):
    # check if first letter of name is R
    if name[0] == 'R':
        return name

resulting_names = list(filter(names_check, all_names))

print(resulting_names)