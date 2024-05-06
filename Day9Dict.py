# Dictionary / HashMap

# Key: Value pair
# Keys should be unqiue

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