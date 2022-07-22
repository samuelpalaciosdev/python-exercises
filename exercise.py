all_colors = [
	{"label": 'Red', "sexy": True},
	{"label": 'Pink', "sexy": False},
	{"label": 'Orange', "sexy": True},
	{"label": 'Brown', "sexy": False},
	{"label": 'Pink', "sexy": True},
	{"label": 'Violet', "sexy": True},
	{"label": 'Purple', "sexy": False},
]

def filter_colors():
    # check if sexy property is true
    sexy_colors = list(filter(lambda color: color["label"] if color["sexy"] == True else None, all_colors))
    # return only the label
    sexy_colors = list(map(lambda color: color['label'], sexy_colors))
    return sexy_colors
    
def generate_li(colors):
    last_index = len(colors)
    new_list = []
    # for each color, create a li
    for i in range(last_index):
       new_list.append(f'<li>{colors[i]}</li>')
    return new_list
      

print(generate_li(filter_colors()))
    

