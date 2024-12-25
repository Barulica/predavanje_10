import json

with open("data/users.json", 'r') as file:
    data = json.load(file)

print(data[1]['name'])

with open("data/users.json", 'w') as file:
    json.dump(data, file, indent=4)
    data.append({'name': 'Tolima', 'age': 25, "height": 160, "gender": "male"})

print(data)

from methods import load_file, save_file

data = load_file('data/products.json')

print(data)

data.append({'name': 'Marko', 'age': 25, "height": 160, "gender": "male"})

save_file('data/users.json', data)

