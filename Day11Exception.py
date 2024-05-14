
from datetime import datetime
# All the syntax error will give compile time error

# try and except block to handle errors
def mathdivide(n1,n2):
    try:
        #Business Logic error
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



def calAge():
    try:
        byear = int(input("Enter your birth year: "))
        if byear <= 0 or byear > datetime.now().year:
            raise ValueError("Give a valid year")
        age = datetime.now().year - int(byear)
        print(f"Your age is {age}")
    except ValueError as e:
        print(e)

# Creating own error class
# Every error has same base class exception
class NegativeNumberError(Exception):
    def __init__(self, value):
        self.value = value
        self.message = "Negative Numbers are not allowed"
        super().__init__(self.message)
    
    def __str__(self):
        return f"{self.value} -> {self.message}"

def only_positive_nums():
    try:
        x = -10
        if x < 0:
            raise NegativeNumberError(x)
    except NegativeNumberError as err:
        print(err)

if __name__ == '__main__':
    calAge()
    print(datetime.now())
    print(datetime.now().weekday())
    print(datetime.now().year)
    print(mathdivide(10,0))
    print(mathdivide(15,3))
    only_positive_nums()
