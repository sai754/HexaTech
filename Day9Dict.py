# Dictionary / HashMap

# Key: Value pair
# Keys should be unqiue
# Does not allow duplicate keys
person = {
    "name": "Lionel Messi",
    "age":36,
    "country":"Argentina",
    "sport":"Football"
}

# Accessing
print(person["name"])
print(person["country"])


# Update value
person["age"] += 1;
print(person)

# Methods
print(person.keys())
print(person.values())


# Loop through the dictionary
for key in person:
    print(key, person[key])

# Loop by unpcaking the tuple which is returned by the items()
for k,v in person.items():
    print(k,v)

person2 = {
    "name": "Lionel Messi",
    "age": 36,
    "address": {
        "city": "rosario",
        "country": "Argentina",
    },
    "sport": "football",
}

print(person2["address"]["city"])

# Accessing values through [] will result in error if no such key exists

# Safer way to access value is get()
# It will result in None if no such key exists
print(person.get("Cityy"))
print(person.get("name"))

# Default Value
# get() has 2 parameter, the 2nd parameter is default value
# If there is no such key, the the default value is returned
print(person.get("height",172))
print(person.get("stats",{}).get("goals"))
