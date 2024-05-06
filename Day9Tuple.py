# Tuples

# Tuples are immutable
person = ("Sanjana","India",20)

print(person[0])

# Remove - pop(), remove() cannot be used
# Add - append(), insert() cannot be used

# Methods that can be used

# Count, index
print(person.count(20))
print(person.index("India"))

# Index will give error if there is no such element
# Find will return -1 if no such element is present

