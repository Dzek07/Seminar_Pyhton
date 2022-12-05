import json

def save_bd(data):
    data_json = json.dumps(data)

    with open("baza.json", "w") as my_file:
        my_file.write(data_json)

def read_bd():
    with open("baza.json", "r") as my_file:
        data_json = my_file.read()
    data = json.loads(data_json)
    return(data)
