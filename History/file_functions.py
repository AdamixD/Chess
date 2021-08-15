import json

def write_to_file(data, file_name):
    with open(file_name, 'w') as file:
        json.dump(data, file)

def read_from_file(file_name):
    with open(file_name, 'r') as file:
        jsonObject = json.load(file)
