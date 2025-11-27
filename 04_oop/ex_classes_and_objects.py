


# EXERCISES — CLASSES AND OBJECTS IN PYTHON
 
# Goal: practice, review and understand everything learned.
 
 
# EXERCISE 1 — Person class
 
# Create a Person class with attributes: name, age and country.
# Create two objects and print their name and age.
 

class Person:
    def __init__(self, name, age, country=None):
        self.name = name
        self.age = age
        self.country = country


person_1 = Person("Pedro", 29)
print(person_1.name)
print(person_1.age)

person_2 = Person("Carlota", 31)
print(person_2.name)
print(person_2.age)


 
# EXERCISE 2 — Rectangle class

# Create a Rectangle class with attributes width and height.
# Add a method area() that returns the area.
# Create an object and print its area.
 

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


my_rectangle = Rectangle(8, 10)
print(my_rectangle.area())


 
# EXERCISE 3 — BankAccount class
 
# Create a class with methods:
# - deposit(amount)
# - withdraw(amount)
# - show_balance()
 

class BankAccount:
    def __init__(self, balance=0):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def show_balance(self):
        print(self.balance)


# Example usage:
account = BankAccount()
account.deposit(100)
account.withdraw(30)
account.show_balance()


 
# EXERCISE 4 — Car class with class attribute
 
# If it goes over the maximum speed, print "Speed limit reached".
 

class Car:
    max_speed = 180  # class attribute (same for all cars)

    def __init__(self, brand, speed=0):
        self.brand = brand
        self.speed = speed

    def show_speed(self):
        if self.speed >= Car.max_speed:
            print(f"Speed limit reached ({self.speed} km/h)")
        else:
            print(f"Current speed: {self.speed} km/h")

    def accelerate(self, increment):
        self.speed += increment
        if self.speed > Car.max_speed:
            print(f"Speed limit reached ({self.speed} km/h)")
        else:
            print(f"Now you are going at {self.speed} km/h")

    def brake(self, amount):
        if amount <= self.speed:
            self.speed -= amount
            print(f"You braked {amount} km/h. New speed: {self.speed}")
        else:
            self.speed = 0
            print("The car has stopped completely.")


bmw12 = Car("BMW", 110)
bmw12.show_speed()
bmw12.accelerate(80)
bmw12.brake(50)

 
# EXERCISE 5 — Inspect objects
 
# Use dir() and __dict__ to explore the attributes of an object.
 

print(dir(bmw12))
print(bmw12.__dict__)


 
# EXERCISE 6 — Product class and sorting objects
 
# Create a Product class with name and price.
# Create several products and sort them by price using .sort().
 

class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price


carpet = Product("Carpet", 30)
tshirt = Product("T-shirt", 25)
trousers = Product("Trousers", 18)

products = [carpet, tshirt, trousers]

products.sort(key=lambda p: p.price)

for p in products:
    print(p.name, p.price)


 
# EXERCISE 7 — File class with error handling
 
# Create a File class with method read(filename)
# - Try to open a file
# - Catch FileNotFoundError if it does not exist
 

class FileReader:
    def __init__(self, filename):
        self.filename = filename

    def read(self):
        try:
            with open(self.filename, "r", encoding="utf-8") as f:
                content = f.read()
                print(content)
        except FileNotFoundError:
            print("Error: file does not exist.")


# Example usage:
# file_reader = FileReader("example.txt")
# file_reader.read()


 
# BONUS — ETL class (mini data flow)
 
# Simulate a small ETL (Extract, Transform, Load) flow.
# Methods:
# - extract()
# - transform()
# - load()
# - run() → calls the three in order
 

class ETL:
    def __init__(self):
        self.raw_data = None
        self.transformed_data = None

    def extract(self):
        # Simple simulation of an extract step
        self.raw_data = [1, 2, 3, 4, 5]
        print("Extract step: raw data loaded.")

    def transform(self):
        # Simple transformation: square each value
        if self.raw_data is None:
            print("No data to transform.")
            return
        self.transformed_data = [x ** 2 for x in self.raw_data]
        print("Transform step: data transformed.")

    def load(self):
        # Simple load simulation: just print the final data
        if self.transformed_data is None:
            print("No data to load.")
            return
        print("Load step: final data ready:")
        print(self.transformed_data)

    def run(self):
        self.extract()
        self.transform()
        self.load()


# Example usage:
etl_pipeline = ETL()
etl_pipeline.run()

 
# EXERCISE — SentenceAnalyzer class
 
# Create a class that receives a text and:
# 1) Counts how many sentences there are (separated by ".", "!" or "?")
# 2) Counts how many words there are in total
# 3) Has a summary() method that prints both values
 

class SentenceAnalyzer:
    
    def __init__(self, text):
        self.text = text

    def count_sentences(self):
        count = 0
        for ch in self.text:
            if ch in ".!?":
                count += 1
        return count

    def count_words(self):
        words = self.text.split()
        return len(words)

    def summary(self):
        sentences = self.count_sentences()
        words = self.count_words()
        print(f"Number of sentences: {sentences}")
        print(f"Number of words: {words}")


# Example usage:
example_text = "Hello. How are you? I am fine!"
analyzer = SentenceAnalyzer(example_text)
analyzer.summary()


 
# EXERCISE — Cleaner class
 
# Create a class that receives a text and has methods:
# 1) remove_digits() → remove numbers
# 2) remove_symbols() → remove symbols like @, #, $, %, &
# 3) clean_all() → run both methods
# 4) show() → print the cleaned text
 

class Cleaner:
    
    def __init__(self, text):
        self.text = text

    def remove_digits(self):
        cleaned = "".join(ch for ch in self.text if not ch.isdigit())
        self.text = cleaned

    def remove_symbols(self):
        symbols = "@#$%&"
        cleaned = "".join(ch for ch in self.text if ch not in symbols)
        self.text = cleaned

    def clean_all(self):
        self.remove_digits()
        self.remove_symbols()

    def show(self):
        print(self.text)


# Example usage:
dirty_text = "Hello123 @world# this$ is% a& test 2025"
cleaner = Cleaner(dirty_text)
cleaner.clean_all()
cleaner.show()

