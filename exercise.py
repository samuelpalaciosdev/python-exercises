spanish_translations = { "dog": "perro", "house": "casa", "cat": "gato" }

keys = ["love", "code ", "smart"]
values = ['amor', 'codigo', 'inteligente']

for i in range(len(keys)):
    spanish_translations[keys[i]] = values[i]

print("Translation", spanish_translations["dog"])
print(spanish_translations)