# Abstract or Interface
# Force other class to implement certain methods
# Autocomplete
from abc import ABC, abstractmethod
 
 
# Abstract class / Interface
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
 
    @abstractmethod
    def move(self):
        pass
 
 
class Dog(Animal):
    def make_sound(self):
        print("Woof Woof")
 
    def move(self):
        print("Runnning... 🐕")
 
    def jump(self):
        print("Jumps 🦘")
 
 
maxy = Dog()
maxy.move()

class Bird(Animal):
    def make_sound(self):
        print("Kiii Kiiii")
 
    def move(self):
        print("Flying.......")
 
    def eat(self):
        print("Eatingg...🪱")

sparrow = Bird()
sparrow.make_sound()
sparrow.move()
sparrow.eat()