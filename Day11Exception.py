
# All the syntax error will give compile time error

# try and except block to handle errors
def mathdivide(n1,n2):
    try:
        if(n1<0): # Throwing an error
            raise ValueError("Number cannot be negative")
        result=  n1 / n2
    except ZeroDivisionError:
        return "Cannot Divide by zero"
    except ValueError as e:
        return f"Invalid Number: {e}"
    else:
        # When no error happens
        print("Division was successful")
    finally:
        # It will execute 
        #irrespective if there is an error or not
        print("Done")
    return result

print(mathdivide(10,0))
print(mathdivide(15,3))

from datetime import datetime

print(datetime.now())

print(datetime.now().weekday())
print(datetime.now().year)

def calAge():
    byear = int(input())
    try:
        age = datetime.now().year - byear
        print(f"Your age is {age}")
    except ValueError:
        print("Give only numbers as input")

calAge()