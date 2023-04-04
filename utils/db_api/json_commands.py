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
            'user_id': user_id
        })

        # write the updated JSON string to the file
        with open('data.json', 'w') as f:
            json.dump(data, f, indent=2)