# Sets
# Similar to Lists
# Mutable but always unique
# There is no order

# tech_gadgets = {} -> this is not considered as empty set but as a dict


tech_gadgets = {"Smartphone","Laptop","Smartwatch","Tablet","Tablet"}
emptySet = set() # empty set

print(type(tech_gadgets))

tech_gadgets.add("E-reader")
tech_gadgets.add("Laptop")
print(tech_gadgets)

# Find all unique colors
colors = ['red','blue','red','green','pink','blue']
unique = set(colors)
print(unique)

unique2 = set()
for color in colors:
    unique2.add(color)
print(unique2)