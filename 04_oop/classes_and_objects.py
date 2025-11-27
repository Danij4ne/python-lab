# Objects and Classes
# Why classes are used:
#   1- Organize code (cleaner, reusable, easier to maintain).
#   2- Group data and behaviors that belong to the same entity.
#   3- Simulate real-world objects (users, products, animals, etc.).

# .sort() = sort
# .reverse() = reverse list order


class Circle:  # we create a Circle class (the blueprint for creating circles)
    def __init__(self, color, height, width):  # it will receive color, height and width as attributes
        self.height = height
        self.width = width
        self.color = color


RedCircle = Circle("red", 10, 10)

# RedCircle is an object of the class Circle

print(RedCircle.color)
print(RedCircle.height)
print(RedCircle.width)


# Now we create a Car class with a function

class Car:
    def __init__(self, color, brand, speed):
        self.color = color
        self.brand = brand
        self.speed = speed

    def accelerate(self):
        self.speed += 10  # every time accelerate() is called, speed increases by 10
        print(f"The car {self.brand} is now going at {self.speed} km/h")


my_car = Car("red", "Toyota", 100)
your_car = Car("blue", "BMW", 120)

my_car.accelerate()
your_car.accelerate()


# dir = directory, used to inspect what is inside an object (its methods, attributes, etc.)

print(dir(my_car))
# Python shows both what you wrote and what it inherits from the base class "object"


# Class for cleaning text inside an object

class TextAnalyzer:
    
    def __init__(self, text):
        # 1 Store original text
        self.text = text

        # 2 Clean text: remove punctuation
        formattedText = text.replace('.', '').replace('!', '').replace('?', '').replace(',', '')

        # 3 Convert everything to lowercase so "Hello" and "hello" count as the same word
        formattedText = formattedText.lower()

        # 4 Store cleaned text inside the object
        self.fmtText = formattedText


    # 1 METHOD: freqAll()
    # Returns a dictionary with ALL words and their frequencies.
    def freqAll(self):
        wordList = self.fmtText.split(' ')
        freqMap = {}

        for word in set(wordList):  # remove duplicates
            freqMap[word] = wordList.count(word)

        return freqMap


    # 2 METHOD: freqOf(word)
    # Returns how many times a specific word appears.
    # If it does not exist, returns 0.
    def freqOf(self, word):
        freqDict = self.freqAll()

        if word in freqDict:
            return freqDict[word]
        else:
            return 0



# PYTHON — CLASSES AND OBJECTS (Complete summary with examples)

# Python is an object-oriented language (OOP)
# → Code is organized using "classes" and "objects".

# A CLASS = the blueprint
# An OBJECT = a real instance created from that blueprint


# 1 CREATE A CLASS

class Car:
    max_speed = 120  # class attribute (shared by all cars)

    def __init__(self, brand, model, color, speed=0):
        self.brand = brand
        self.model = model
        self.color = color
        self.speed = speed  # default speed is 0

    # 2 INSTANCE METHODS (actions the object can do)

    def accelerate(self, increment):
        if self.speed + increment <= Car.max_speed:
            self.speed += increment
        else:
            self.speed = Car.max_speed
        print(f"{self.brand} {self.model} is now going at {self.speed} km/h")

    def brake(self, decrement):
        if self.speed - decrement >= 0:
            self.speed -= decrement
        else:
            self.speed = 0
        print(f"{self.brand} {self.model} braked and is now going at {self.speed} km/h")

    def get_speed(self):
        return self.speed

    def info(self):
        print(f"{self.brand} {self.model} | Color: {self.color} | Speed: {self.speed} km/h")


# 3 CREATE OBJECTS (INSTANCES)

car1 = Car("Toyota", "Camry", "Blue")
car2 = Car("Honda", "Civic", "Red", 50)


# 4 INTERACT WITH OBJECTS

car1.accelerate(30)
car2.accelerate(20)

car1.brake(10)
car2.brake(100)

print(car1.get_speed())
print(car2.get_speed())

car1.info()
car2.info()


# 5 ACCESS ATTRIBUTES

print(car1.color)

car1.color = "Black"
print(car1.color)

print(Car.max_speed)


# 6 USEFUL FUNCTIONS TO INSPECT OBJECTS

print(dir(car1))     # all attributes and methods
print(car1.__dict__) # only custom attributes
print(type(car1))    # <class '__main__.Car'>


# 7 FINAL SUMMARY

# Class = blueprint
# Object = instance created from the class
# Attributes = data inside the object
# Methods = actions the object can perform
# self = reference to the object itself
# Instancing = creating an object (car1 = Car(...))
# Class attribute = shared by all objects (Car.max_speed)
# Instance attribute = specific to one object (car1.color)

