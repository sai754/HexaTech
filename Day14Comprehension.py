colors = ["red","blue","red","green","pink","blue"]


# using add
unique_colors = set()
for color in colors:
    unique_colors.add(color)

# set comprehension
unique_colors_1 = {clr for clr in colors}
print(unique_colors_1)   

words = ["This", "is", "cool", "mangoes", "oranges", "apple"]

word_len = { len(word) for word in words}
print(word_len)

# Dictionary Comprehension

squares = {x: x**2 for x in range(1,5)}
print(squares)

# Tasks

classes = {
    "Class A": [
        {"name": "Alice", "grades": [82, 90, 88]},
        {"name": "Bob", "grades": [78, 81, 86]},
        {"name": "Charlie", "grades": [85, 85, 87]},
        {"name": "Alex", "grades": [85, 90, 87]},
    ],
    "Class B": [
        {"name": "Dave", "grades": [92, 93, 88]},
        {"name": "Eve", "grades": [76, 88, 91]},
        {"name": "Frank", "grades": [88, 90, 92]},
    ],
}

def find_avg(items):
    return round(sum(items)/len(items),2) 

class_avg = {}
for class_name, students in classes.items():
    class_student_avg = []
    for student in students:
        avg = find_avg(student["grades"])
        class_student_avg.append(avg)
    class_avg[class_name] = find_avg(class_student_avg)
 
print(class_avg)

# Task 1.1 list comprehenion

# class_avg1 = {}
# for class_name, students in classes.items():
#     class_student_avg = [ find_avg(student["grades"] for student in students)]
#     class_avg1[class_name] = find_avg(class_student_avg)
# print(class_avg1)


# Dictionary comprehension

# class_avg2 = {
#     class_name: find_avg([find_avg(student["grades"]) for student in students])
#     for class_name, students in classes.items()
# }
 
# print(class_avg2)

# Task 2: Find average of each student
output = {
    "Class A": {"Alice": 90.50, "Bob": 84.50, "Charlie": 90.00},
    "Class B": {"Dave": 92.50, "Eve": 86.50, "Frank": 950},
}
 
output = {}

for class_name, students in classes.items():
    class_avg = {}
    for student in students:
        name = student["name"]
        avg_grade = sum(student["grades"]) / len(student["grades"])
        class_avg[name] = round(avg_grade, 2)
    output[class_name] = class_avg

print(output)