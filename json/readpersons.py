import json
with open("persons.json", "r") as read_file:
    data = json.load(read_file)
    print(data[0]['fname'])
