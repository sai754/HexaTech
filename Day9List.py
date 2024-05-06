# List or Array

marks = [98,75,40,80,90,45,80,60]

print(type(marks))
print(len(marks))
print(marks[1])
print(marks[-1])

# Slicing operator works here too : 

print(marks[:4])
print(marks[::-1])

# List are used to store multiple values in a single variable
# we can have list of strings, list of integers, list of lists too

# Methods of Lisis
# 1. append() - adds at the end of the list
marks.append(78)

# 2. insert(index,value) - adds at a specific location
m = 65
marks.insert(3,65)
print(marks)

# 3. '+' can be used to merge two lists together

grocery_list = [1000,1500,400]
fruits_list = [2000,500]

final_list = grocery_list + fruits_list

print(final_list)

# Remove elements from the list
# pop(index) - Removes element from a particular index
# If no index is specified then it will remove the last element

heights = [198,175,140,177]
heights.pop()

# remove(value) - It can also be used to remove elements from the list
# We have to specify the value
# If there are more than one item with the value then it will remove the 
# first occurance

heights.remove(198)

# Lists are mutable

heights[0] = 190

price_list= [1000,1500,400] #price list
price_list_copy = price_list #price list copy 1
# Copy by Reference
# If price_list_copy is changed then price_list will also be changed

price_list1 = [1000,1500,400]

price_list_copy.append(600)
price_list.append(700)
price_list1.append(800)

print(price_list,price_list_copy,price_list1)

# Copy by Value

p1 = [1000,1500,400]
p2 = p1.copy()
# or
p3 = p1[:]
print(id(p1),id(p2)) #id is used to find the address

# Repetition
cloned = ['Gold Coin'] * 3
print(cloned)

# split (str to List) vs join

shop_stock = "Vanilla,Lime,Chocolate"
shop_stock_List= shop_stock.split(",")

print(shop_stock_List)

# join (list to str)

avatar = ['Fire','Water','Earth','Air']
print(",".join(avatar))
print("!".join(avatar))

avatar[1:3] = ['Diamond','Platinum','Gold']
print(avatar)

