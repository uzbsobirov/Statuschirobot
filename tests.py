import json

# Open the JSON file for reading
with open('data.json', 'r') as file:
    # Parse the contents of the file into a Python object
    data = json.load(file)

# Iterate over the array of objects and check if the "id" key is equal to 1
for row in data:
    if row['user_id'] == 1435473812:
        # If a matching object is found, store it in a variable or perform the desired operations on it
        row['full_name'] = 'Anvar'
        matching_row = row
        break

with open('data.json', 'w') as file:
    json.dump(data, file)



# Print the matching row for demonstration purposes
# print(matching_row)
