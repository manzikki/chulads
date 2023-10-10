import json
with open("person.json", "r") as read_file:
    data = json.load(read_file)
    print(data)
