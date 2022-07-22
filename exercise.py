incoming_ajax_data = [
	{ "name": 'Mario', "last_name": 'Montes' },
	{ "name": 'Joe', "last_name": 'Biden' },
	{ "name": 'Bill', "last_name": 'Clon' },
	{ "name": 'Hilary', "last_name": 'Mccafee' },
	{ "name": 'Bobby', "last_name": 'Mc birth' }
]

def data_transformer(dicts):
    new_list = list(map(lambda x: f"{x['name']} {x['last_name']}", dicts))
    return new_list

print(data_transformer(incoming_ajax_data))
# ['Mario Montes', 'Joe Biden', 'Bill Clon', 'Hilary Mccafee', 'Bobby Mc birth']