# File Handling

import json


bank_data = """
[
    {
        "id": 1,
        "name": "John Doe",
        "email": "johndoe@example.com",
        "isActive": true,
        "balance": 150.75
    },
    {
        "id": 2,
        "name": "Jane Smith",
        "email": "janesmith@example.com",
        "isActive": false,
        "balance": 500.50
    },
    {
        "id": 3,
        "name": "Emily Jones",
        "email": "emilyjones@example.com",
        "isActive": true,
        "balance": 0.00
    }
]
"""

# json.loads -> Converts json to dictionary
# json.dumps -> Converts dictionary to json

bank_data_dict = json.loads(bank_data)
#print(bank_data_dict)

# Task 1 (normal for loop)
# All Active user's balance should increase by 10%
# Final Output should be JSON format

for i in bank_data_dict:
    #print(i)
    if i["isActive"] == True:
        i["balance"] +=  i["balance"] * 0.10
    else:
        continue

bank_data1 = json.dumps(bank_data_dict)
print(bank_data1)

# open() - write / read file
# with - auto close the file no matter what
# open("filename","mode of operation")
# dump is used to write as a json file

# with open("bank_accounts.json","w") as file:
#     json.dump(bank_data_dict,file,indent=4)

# Read from a file

with open("bank_accounts.json","r") as file:
    data = json.load(file)
    print(data)

# json.dumps  -> dumps as JSON
# json.dump  -> dumps as file (JSON)
# json.loads  -> loads into dict
# json.load  -> read as file (dict)

# CSV

import csv
 
with open("citizens.csv", "w", newline="") as file:
    writer = csv.writer(file)  # json.dump
    writer.writerows(data)
 
 
with open("citizens.csv", "r", newline="") as file:
    reader = csv.reader(file)  # json.dump
    data = [row for row in reader]
    print(data)



