books = [
    {
        "title": "Infinite Jest",
        "rating": 4.5,
        "genre": "Fiction"
    },
    {
        "title": "The Catcher in the Rye",
        "rating": 3.9,
        "genre": "Fiction"
    },
    {
        "title": "Sapiens",
        "rating": 4.9,
        "genre": "History"
    },
    {
        "title": "A Brief History of Time",
        "rating": 4.8,
        "genre": "Science"
    },
    {
        "title": "Clean Code",
        "rating": 4.7,
        "genre": "Technology"
    },
]

# Task 1: Highly Rated books i.e more than 4.7

rate = []
for book in books:
    if book['rating'] >=4.7:
        rate.append(book['title'])
print(rate)

rate2 = [book['title'] for book in books if book['rating'] >=4.7]
print(rate2)
