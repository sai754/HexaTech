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

# Update() can be used to add multiple elements to sets

all_tech_gadget = {"Smartphone","Laptop","Smartwatch"}
more_gadget = {"Drone","Selfiestick"}

all_tech_gadget.update(more_gadget)

# Delete
# remove() - error | discard() - safer

all_tech_gadget.discard("Drone")

# working across sets
# 1. Union - outdoor_activities.union(indoor_activities)
# 2. Intersection
# 3. Difference
# 4. symmetric_difference (removes the common element)

