import json

list_of_dicts = [{'x': 1, 'y': 2}, {'x': 3, 'y': 4}]

list_of_dicts_str = json.dumps(list_of_dicts)

file = open("f.txt", "w")
file.write(list_of_dicts_str)
file.close()

file = open("f.txt", "r")
list_of_dicts_str_form_file = file.read()
file.close()


def read():
    with open("f.txt", "r") as file:
        return json.loads(file.read(), encoding='utf-8')

list_of_dicts_form_file = read()
print(list_of_dicts_form_file[0])