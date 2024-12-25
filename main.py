import json

with open("data/users.json", 'r') as file:
    data = json.load(file)

print(data[1]['name'])

with open("data/users.json", 'w') as file:
    json.dump(data, file, indent=4)
    data.append({'name': 'Tolima', 'age': 25, "height": 160, "gender": "male"})

print(data)

with open("data/products.json", 'r') as file:
    data = json.load(file)
print(data)

