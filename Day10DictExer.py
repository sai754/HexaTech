employees = [
    {"name": "Sneha", "experience": 2},
    {"name": "Manju"},
    {"name": "Sai Subash", "experience": 4},
    {"name": "Manasa"},
]
  
# Task 1: After 1 experience

for e in employees:
    e['experience']= e.get("experience",0)+1

# Task 2:
# Senior 5 or more, Mid-level 3 to 5, junior < 3

for e in employees:
    exp = e.get('experience')
    if exp >= 5:
        e['status'] = 'Senior'
    elif exp < 5 and exp >=3:
        e['status'] = 'Mid-level'
    else:
        e['status'] = 'Junior'
print(employees)
 
# Output
[
    {"name": "Sneha", "experience": 3},
    {"name": "Manju",  "experience": 1},
    {"name": "Sai Subash", "experience": 5},
    {"name": "Manasa", "experience": 1},
]