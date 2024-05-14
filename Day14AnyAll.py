print(all([True,False,True])) # False - like 'and'
print(any([True,False,True])) # True - like 'or'

marks = [50, 50, 50, 90]

if all([i>40 for i in marks ]):
    print("Yes, They wil get marks")
else:
    print("No They will not")