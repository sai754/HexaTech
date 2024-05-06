# Used for repeating a set of operations

# While vs For

# i = 1
# while i <= 5:
#     print(i)
#     i = i + 1

# Task 1
count_of_stars = 5
i = 1
while i <= count_of_stars:
    print("✨" * i)
    i = i + 1

# For Loops
# for i in range(start,stop,step)
for i in range(1,10,2):
    print(i)

for i in range(1,count_of_stars+1):
    print("✨" * i)

# Player stats double

player_stats = [10,20,30]

# One Way
for i in range(len(player_stats)):
    player_stats[i] = player_stats[i] * 2

print(player_stats)

# Another way
# values = []
# for i in player_stats:
#     i = i * 2
#     values.append(i)
# print(values)

# List Comprehension - copy of the result

poweredup_stats = [ i * 2 for i in player_stats]
print(poweredup_stats)
print(player_stats)

avengers = [
    "Hulk",
    "Iron man",
    "Black widow",
    "Captain america",
    "Spider man",
    "Thor",
]
 
# Task 4.1 - for loop
h1 = []
for i in avengers:
    h1.append(len(i))
print(h1)

# Task 4.2 - List comprehension
h2 = [len(avenger) for avenger in avengers]
print(h2)

# Task 5.1
# get only height greater than 10
h3 = []
for avenger in avengers:
    if len(avenger) > 10:
        h3.append(avenger)
print(h3)

# Task 5.2
h4 = [avenger for avenger in avengers if len(avenger) > 10]
print(h4)
