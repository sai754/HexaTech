# Multiple variable assignment

a = b = c = 10

print(a,b,c)


# Matching by the index values
# unpacking
p, s, sa = ("Black Current","Choco Chip","Butterscotch")

print(p)
print(s)

#t1,t2,t3= [100,200,300,400] # this will error out

#print(t1,t2,t3)

# * -> unpacking operator
# it will put all the remaining item in t3
# t3 will become a list
t1,t2,*t3 = [100,200,300,400,60,40]

print(t1,t2,t3)

# Task 1

coordinates = [(5,4),(1,1),(6,10),(9,10)]

# Task 1.1 use normal for loop
dist = []
for i in coordinates:
    dist.append((i[0]**2+i[1]**2)**0.5)
print(dist)

# Task 1.2 for loop + unpacking
# d = []
# for i in coordinates:
#     x,y = i
#     d.append((x**2+y**2)**0.5)
# print(d)

d = []
for x,y in coordinates:
    d.append((x**2+y**2)**0.5)
print(d)

# Task 1.3 List Comprehension

d1 = [round((x**2+y**2)**0.5,2) for x,y in coordinates]
print(d1)

# If u want only the last element in t3
t1,t2,*_,t3 = [100,200,300,400,60,40]

print(t1,t2,t3)


# 3rd way to copy lists
# Using unpacking operator
# 1st - using Copy() method
# 2nd - using slicing operator [:]
marks1 = [70,80,60]
marks2 = [*marks1,40,50]
print(marks2)

# Task

t1 = [80,90]
t2 = [50,60]
t3 = [*t1,*t2]
print(t3)

# unpacking operator for dictionary -> **

movie = { 'name': 'John Wick', 'year':2014 }
m1 = {**movie, "actor":"Keanu Reeves"}
m2 = {**movie, "actor":"Keanu Reeves", 'year':2015}
# Dictionary only have unique keys
# So if the key is repeated it will be overwritten
m3 = {"actor":"Keanu Reeves", 'year':2015, **movie}
print(movie)
print(m1)
print(m2)
print(m3)