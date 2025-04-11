import json


name = input("Enter name: ")
age = input("Enter age: ")
address = input("Enter address: ")
number = input("Enter phone number: ")
email = input("Enter email: ")

info_dict = {"name": name, 
             "age": age, 
             "address" : address, 
             "number" : number, 
             "email" : email}

json_info = json.dumps(info_dict)

with open('personal_info.json', 'w') as json_file:
    json.dump(json_info, json_file)

with open('personal_info.json', 'r') as json_file:
    loaded_file = json.load(json_file)
print(loaded_file)