import json

class Database:


    async def add_user(self, full_name, username, user_id):
        # read the existing JSON file
        with open('data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)

        # add new data to the Python object
        data.append({
            'full_name': full_name,
            'username': username,
            'user_id': user_id,
            'text_size': 0,
            'text_color': 'yellow',
            'text_place': 'center',
            'text_shrift': 0
        })

        # write the updated JSON string to the file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)

    async def update_user(self, user_id, full_name):
        # Open the JSON file for reading
        with open('data.json', 'r') as file:
            # Parse the contents of the file into a Python object
            data = json.load(file)

        # Iterate over the array of objects and check if the "id" key is equal to 1
        for row in data:
            if row['user_id'] == user_id:
                # If a matching object is found, store it in a variable or perform the desired operations on it
                row['full_name'] = full_name
                break

        with open('data.json', 'w') as file:
            json.dump(data, file)