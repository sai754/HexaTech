# Idea
# Object Oriented Programming
# Modeling our problem as real-world objects
 
# Car
# What makes a car?
# 1. engine
# 2. wheels
# 3. name
# 4. doors
 
 
#  Car
# 1. engine - v8
# 2. wheels - 4
# 3. name - Ferrari
# 4. doors - 2
 
 
# 1. engine - v4
# 2. wheels - 4
# 3. name - Alto
# 4. doors - 4
 
 
#  Car -> blueprint | Class blueprint object
 
 
class Car:
    def __init__(self, name, engine, wheels, doors):  # creating object calls init (constructor)
        # creating object calls __init__ (constructor)
        # Instance Variables
        self.name = name
        self.engine = engine
        self.wheels = wheels
        self.doors = doors
    # instance method
    def horn(self):
        return f"{self.name} says vroom vroom"
 

ferrari = Car("Ferrari", "v8", 4, 2)  # object
alto = Car("Alto", "v4", 4, 4)  # object
lambo = Car("Lamborgini","v8",4,2)
koenigsegg = Car("koenigsegg","v12",4,2)
 
print(ferrari.name, ferrari.wheels)

print(lambo.horn())

# Task
# Bank account
# acc_no, name, balance

# Encapsulation: Putting everything together in a single entity i.e class
class Bank:
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def display_balance(self):
        return f"Your balance is: ₹ {self.balance:,}"
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return f"Success!. Your balance is now {self.balance:,}"
        else:
            return "Not enough Balance"
    def deposit(self,amt):
        self.balance += amt
        return f"Success!. {self.display_balance()}"
    
akash = Bank("Akash",112345678911,70000)
rex = Bank("Rex",223564789123,72000)
alen = Bank("Alen",336547891234,73000)

print(akash.name, akash.acc_no)
print(alen.withdraw(100))
print(alen.deposit(3000))

class Bank1:
    # Class Variables, All the class variables will share the class variables
    interest_rate = 0.02
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
    def display_balance(self):
        return f"Your balance is: ₹ {self.balance:,}"
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return f"Success!. Your balance is now {self.balance:,}"
        else:
            return "Not enough Balance"
    def deposit(self,amt):
        self.balance += amt
        return f"Success!. {self.display_balance()}"
    
    def apply_interest(self):
        self.balance += (self.balance * Bank1.interest_rate)
        return f"Your Balance is now {self.display_balance()}"

sai = Bank1("Sai",132456789222,80000)
abash = Bank1("Abash",456789123130,85000)

print(abash.apply_interest())

# Static Method vs Class Methods  = Both are decorators

# Static method: 
# Normal function
# It does not deal with any class instances like "self" but still use it 
# inside a class
# use @staticmethod to mark it as static
class Circle:
    pi = 3.14
    def __init__(self, radius):
        self.radius = radius
 
    @staticmethod # Does not have access to cls instances 
    def perimeter(radius):
        return 2 * Circle.pi * radius
 
    @classmethod # Modify the class variables | Create objects
    def from_diameter(cls, diameter):
        r = diameter / 2
        return cls(r)
 
    def calculate_area(self):
        return Circle.pi * self.radius**2
 
 
# Normal function but inside class | no access to self
# static method
print(Circle.perimeter(2))
 
# Instance method
circle1 = Circle(4)
print(circle1.calculate_area())
 
# Class method - to construct the object | modify the class variables
circle_from_dia = Circle.from_diameter(10)
print(circle_from_dia.calculate_area())  # 78.5

class Bank2:
    # Class Variables, All the class variables will share the class variables
    interest_rate = 0.02
    count = 0
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.acc_no = acc_no
        self.balance = balance
        Bank2.count+=1
    def display_balance(self):
        return f"Your balance is: ₹ {self.balance:,}"
    def withdraw(self, amt):
        if amt <= self.balance:
            self.balance = self.balance - amt
            return f"Success!. Your balance is now {self.balance:,}"
        else:
            return "Not enough Balance"
    def deposit(self,amt):
        self.balance += amt
        return f"Success!. {self.display_balance()}"
    
    def apply_interest(self):
        self.balance += (self.balance * Bank2.interest_rate)
        return f"Your Balance is now {self.display_balance()}"
    @staticmethod
    def get_total_accts():
        print(Bank2.count)
    
    @classmethod
    def update_interest(cls,intr):
        cls.interest_rate = intr
        print(cls.interest_rate)

# Get total number of accounts()
# update my interest rate

sai = Bank2("Sai",132456789222,80000)
abash = Bank2("Abash",456789123130,85000)

#Bank2.get_total_accts()
Bank2.update_interest(0.02)

# Access modifiers

# Public  
# Private -> __ (double underscore)
# Protected -> _ (single underscore)

class Bank3:
    # Class Variables, All the class variables will share the class variables
    __interest_rate = 0.02
    __count = 0
    def __init__(self,name,acc_no,balance):
        self.name = name
        self.__acc_no = acc_no
        self.__balance = balance
        Bank3.__count+=1
    def display_balance(self):
        return f"Your balance is: ₹ {self.__balance:,}"
    def withdraw(self, amt):
        if amt <= self.__balance:
            self.__balance = self.__balance - amt
            return f"Success!. Your balance is now {self.__balance:,}"
        else:
            return "Not enough Balance"
    def deposit(self,amt):
        self.__balance += amt
        return f"Success!. {self.display_balance()}"
    
    def apply_interest(self):
        self.__balance += (self.__balance * Bank3.__interest_rate)
        return f"Your Balance is now {self.display_balance()}"
    @staticmethod
    def get_total_accts():
        print(Bank3.__count)
    
    @classmethod
    def update_interest(cls,intr):
        cls.__interest_rate = intr
        print(cls.__interest_rate)

sai1 = Bank3("Sai",132456789222,80000)
abash1 = Bank3("Abash",456789123130,85000)

Bank3.get_total_accts()

# Conventions
# 1. Privatize all instances and class variables
# 2. Access the class variables through the public methods

# Inheritance

# Protected variables can be used during inheritance if you want
# to inherit the variables or methods
# Private variables cannot be inherited
class Animal:
    def __init__(self,name):
        self._name = name

    def speak(self):
        return "Sounds"

class Dog(Animal):
    def __init__(self,name,speed):
        super().__init__(name) # Calling the base class constructor
        self.speed = speed

    def run(self):
        return "Wags tail"
    
    def speak(self): # Polymorphism: Method Overriding
        return "Woof!!"
    
    def speedbonus(self):
        return f"{self._name} is running at {self.speed * 2} km/hr"

toby = Animal('toby')
print(toby.speak())
#print(toby.run())

maxy = Dog('maxy',20)
print(maxy.run())
print(maxy.speak())
print(maxy.speed)
print(maxy.speedbonus())

# Task 

class Bank4:
    # Class Variables, All the class variables will share the class variables
    _interest_rate = 0.02
    _count = 0
    def __init__(self,name,acc_no,balance):
        self.name = name
        self._acc_no = acc_no
        self._balance = balance
        Bank4._count+=1
    def display_balance(self):
        return f"Your balance is: ₹ {self._balance:,}"
    def withdraw(self, amt):
        if amt <= self._balance:
            self._balance = self._balance - amt
            return f"Success!. Your balance is now {self._balance:,}"
        else:
            return "Not enough Balance"
    def deposit(self,amt):
        self._balance += amt
        return f"Success!. {self.display_balance()}"
    
    def apply_interest(self):
        self._balance += (self._balance * self._interest_rate)
        return f"Your Balance is now {self.display_balance()}"
    @staticmethod
    def get_total_accts():
        print(Bank4._count)
    
    @classmethod
    def update_interest(cls,intr):
        cls._interest_rate = intr
        print(cls._interest_rate)

class SavingsAccount(Bank4):
    _interest_rate = 0.05

sabesh = SavingsAccount("Sabesh",131,80000)
print(sabesh.apply_interest())

class CurrentAccount(Bank4):
    def withdraw(self, amt):
        return super().withdraw(amt+10)
    
tanishq = CurrentAccount("tanishq",132,90000)

print(tanishq.withdraw(1000))
print(tanishq.withdraw(10000))
print(tanishq.display_balance())



# Magic methods
# __init__ -> dunder methods | Internally used methods
class Cat():
    def __init__(self,name,speed):
        self.__name = name 
        self.__speed = speed
    
    def __str__(self):
        return f'Hi, I am {self.__name} with speed {self.__speed}'
    
    def __repr__(self):
        return f"Cat('{self.__name}', {self.__speed})"
    
    def __add__(self, other):
        return self.__speed + other.__speed
    
    def speak(self): # Polymorphism: Method Overriding
        return "Meow"
    
pichu = Cat("pichu",30)
snowbell = Cat("snowbell",10)

print(pichu)
print(repr(pichu))
print(repr(snowbell))

print(pichu + snowbell)