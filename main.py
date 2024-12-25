import json

with open("user.json", 'r') as file:
    data = json.load(file)

print(data[1]['name'])

with open("user.json", 'w') as file:
    json.dump(data, file, indent=4)
    data.append({'name': 'Tolima', 'age': 25, "height": 160, "gender": "male"})

print(data)


