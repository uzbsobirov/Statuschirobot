import json

# read the existing JSON file
with open('data.json', 'r', encoding='utf-8') as f:
    data = json.load(f)


# add new data to the Python object
data.append({
    'name': 'John',
    'age': 30,
    'city': 'New York'
})

# write the updated JSON string to the file
with open('data.json', 'w') as f:
    json.dump(data, f, indent=2)
