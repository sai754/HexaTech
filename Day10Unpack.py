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