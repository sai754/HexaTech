# Function
# Declaration / Definition
# Function name
from pprint import pprint
def add(a,b):
    return a + b

print(f"The sum is {add(9,10)}")

def driving_test(name,age,car="Dezire"):
    if age>=18:
        return f"{name} eligible for driving. You will be tested in {car}"
    else:
        return "Try again after few years"

print(driving_test("Sai Subash", 20, "Creata"))
print(driving_test("Sai Ganesh", 20)) # Position Argument

# Types of arguments
# 1. Position Argument
# 2. Keyword argument

print(driving_test(age=20,name="Poojitha")) # Keyword argument

library_list = [
    {
        "title": "Python Programming",
        "author": "Eric Matthes",
        "year": 2019,
        "available": True
    },
    {
        "title": "Automate the Boring Stuff with Python",
        "author": "Al Sweigart",
        "year": 2020,
        "available": True
    },
    {
        "title": "Learning Python I",
        "author": "Mark Lutz",
        "year": 2013,
        "available": False
    },
    {
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "year": 2015,
        "available": True
    },
    {
        "title": "Adavance Python",
        "author": "Mark Lutz",
        "year": 2015,
        "available": False
    },
]
book = {"title": "Fluent Python II", "author": "Alex", "year": 2016, "available": True}

# Task 1
# Add book function: wrte a function add_book(library, new_book)

def add_book(library_list, book):
    library_list.append(book)
    return library_list

print(add_book(library_list, book))

# Task 2 
# Search books by author
# Write a function serach_by_author(library, author_name)

def search_by_author(library, name):
    b = []
    for i in library:
        if i["author"] == name:
            b.append(i)
    return b
print(search_by_author(library_list,"Mark Lutz"))

def searchby_author(library,name):
    return [book for book in library if book['author'] == name]

# Task 3
# Check Out Book Function: 
# Write a function check_out_book(library, title) 
# that marks a book as not available if it exists and is available in the library.

def check_out_book(library, title):
    for i in library:
        if i['title'] == title and i['available'] == True:
            i['available'] = False
            return "Book Checked out"
        elif i['title'] == title and i['available'] == False:
            return "Book Not Available"
    return "Book Does Not Exist"

print(check_out_book(library_list,'Adavance Python'))

# InBuilt Functions
# 1. sum
# 2. max
# 3. min
# 4. len
# 5. round

print(sum([5,6,7,10]))
print(max("abcde"))

movies = [
    {
        "title": "Inception",
        "ratings": [5, 4, 5, 4, 5]
    },
    {
        "title": "Interstellar",
        "ratings": [5, 5, 4, 5, 4]
    },
    {
        "title": "Dunkirk",
        "ratings": [4, 4, 4, 3, 4]
    },
    {
        "title": "The Dark Knight",
        "ratings": [5, 5, 5, 5, 5]
    },
    {
        "title": "Memento",
        "ratings": [4, 5, 4, 5, 4]
    },
]

# Task Average rating for each movie with function

# Task 1, with one funciton

def avg_rating(movies):
    for i in movies:
        i["average_rating"] = sum(i['ratings'])/len(i['ratings'])
    return movies
pprint(avg_rating(movies))

# Task 2, with two functions

def avg_rating2(movie):
    movie['average_rating'] = sum(movie['ratings'])/len(movie['ratings'])
    return movie

def moviesList(movies):
    for i in movies:
        avg_rating2(i)
    return movies

pprint(moviesList(movies))

# for arbitrary position arguments
def own_max(*nums):
    x = nums[0]
    for i in nums:
        if i > x:
            x = i
    return x

print(own_max(5,5,4,3,2,0))

# For arbitrary keyword Arguments
def party(**people):
    print(people.values())

party(p1="A",p2="B",p3="C")

# Lambda functions

add3 = lambda a , b : a+b

print(add3(1,2))