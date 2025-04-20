# def outer():
#     msg = "Hello"

#     def inner():
#         print(msg)
#     inner() #or return inner()

# #function call
# outer()


# def counter():
#     count = 0  # This variable is in the enclosing scope

#     def increment():
#         nonlocal count  # Tell Python to use 'count' from the enclosing function
#         count += 1
#         return count

#     return increment  # Returning the inner function

# counter1 = counter()  # Creates a new counter
# print(counter1())  # Output: 1
# print(counter1())  # Output: 2
# print(counter1())  # Output: 3

# counter2 = counter()  # Creates a separate counter
# print(counter2())  # Output: 1
# print(counter2())  # Output: 2

# def log_decorator(func):
#     def wrapper(*args, **kwargs):  # Wrapper function takes any arguments
#         print(f"Calling {func.__name__} with {args} {kwargs}")  # Logs function name and arguments
#         return func(*args, **kwargs)  # Calls the original function
#     return wrapper  # Returns the wrapper function (not calling it yet!)

# @log_decorator
# def say_hello(name):
#     print(f"Hello, {name}")

# # #This is manual calling by decorator
# # def say_hello(name):
# #     print(f"Hello, {name}")

# # say_hello = log_decorator(say_hello)  # Decorate the function

# say_hello("Alice")

# def uppercase_decorator(func):
#     def wrapper():
#         result = func()
#         return result.upper()
#     return wrapper

# def exclaim_decorator(func):
#     def wrapper():
#         result = func()
#         return result + "!!!"
#     return wrapper

# @uppercase_decorator
# @exclaim_decorator
# def greet():
#     return "hello"

# print(greet())


# def multiplier(factor):
#     value = 1
#     while True:
#         num = yield value * factor  # Multiply by factor
#         if num is not None:
#             value = num  # Update value

# gen = multiplier(5)
# print (gen) # output = <generator object multiplier at 0x000001682C478380>
# next(gen)  #  output=5 ,# Initialize generator

# print(gen.send(2))  # 2 * 5 = 10

# print(gen.send(3))  # 3 * 5 = 15
# print(gen.send(4))  # 4 * 5 = 20


# class Counter:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self  # An iterator must return itself

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration
#         value = self.current
#         self.current += 1
#         return value

# counter = Counter(1, 4)
# print(next(counter))  # Output: 1
# print(next(counter))  # Output: 2
# print(next(counter))  # Output: 3
# print(next(counter))  # Raises StopIteration



# class Counter:
#     def __init__(self, start, end):
#         self.current = start
#         self.end = end

#     def __iter__(self):
#         return self  # Returns itself as an iterator

#     def __next__(self):
#         if self.current >= self.end:
#             raise StopIteration  # Stops when we reach the limit
#         self.current += 1
#         return self.current - 1  # Returns the previous value
#     # Without -1, the generator would return the incremented value instead of the
#     # previous value, meaning the iteration would start from 2 instead of 1.
    
# counter = Counter(1, 5)  # Create an iterator from 1 to 5
# print(next(counter)) # output = 1
# print(next(counter)) # output = 2
# print(next(counter)) # output = 3
# print(next(counter)) # output = 4
# print(next(counter)) # output = 5

# import asyncio

# async def slow_function():
#     print("Start slow task...")
#     await asyncio.sleep(3)  # ✅ Non-blocking, allows other tasks to run
#     print("Task completed!")

# async def main():
#     print("Before calling function")
#     await slow_function()  # ✅ Execution is paused, but program isn't blocked
#     print("After function call")

# asyncio.run(main())  # ✅ Runs async functions properly

# r = range(10**6)  # Creates a lazy iterator, not a list
# print (range(10**6)) # ouput= range(0,1000000) #this is not lazy iterator

# print(r[0])      #output=0 # Accessing does not create a full list
# print(r[17])     #output =17

# def memoize():
#     cache = {}  # Stores previously computed results # <class 'dict'>>

#     def get_square(n):
#         if n not in cache:
#             cache[n] = n * n  # Store 4 as key, 16 as value
#         return cache[n]  # Return cached result

#     return get_square

# square = memoize()
# print(square(4))  # Computes and stores 16
# print(square(4))  # Fetches 16 from cache (no recomputation)
# print(square(16))


# def super_func(*args, **kwargs):
#     print( type(args))
#     print( type(kwargs))
#     return sum(args)

# print(super_func(1,2,3,4,5, x=5,y=6,z=7))

# x ="HELLO"[0]
# print(x) #ouput= H

# class BigObject:
#     pass
# print(type(BigObject))  #<class 'type'>

# obj1=BigObject()
# print(type(obj1)) #<class '__main__.BigObject'>



# class Car:
#     """This is a Car class"""
#     wheels = 4

#     def __init__(self, brand):
#         self.brand = brand  # Instance attribute

# car = Car("Toyota")

# print(car.__dict__)   # output= {'brand': 'Toyota'} (Instance attributes)

# print(Car.__dict__)   # Shows all class attributes


# print(car.__class__)  # output = <class '__main__.Car'> (Metadata about class)

# print(car.__module__) # output = __main__

# print(Car.__doc__)    # output = This is a Car class (Docstring)

# import math

# print(math.__name__)  # "math"
# print(math.__doc__)   # Documentation about the math module
# print(math.__file__)  # File path of the math module


# class MyClass:
#     def __new__(cls):
#         # Call __new__ of the parent class (object)
#         instance = super().__new__(cls)
#         print("New instance is created:", instance)
#         return instance

# obj = MyClass() #output = New instance is created: <__main__.MyClass object at 0x000002175F0F3740>
# print(obj)  #output = <__main__.MyClass object at 0x000002175F0F3740>



# class ImmutableClass:
#     def __new__(cls, value):
#         # Create the instance and set the value during instance creation
#         instance = super().__new__(cls)
#         instance.value = value
#         return instance

#     def __setattr__(self, key, value):
#         # Prevent modifying any attribute once it's set
#         raise AttributeError(f"Cannot modify attribute '{key}', object is immutable")

# obj = ImmutableClass(10)
# print(obj.value)  # 10

# Uncommenting this line will raise an error because modification is not allowed
# obj.value = 20  # This will raise: AttributeError: Cannot modify attribute 'value', object is immutable


# class MyClass(object):
#     pass

# print(MyClass) #ouput : <class '__main__.MyClass'>
# MyClass.

# class SemiImmutableClass:
#     def __new__(cls, value):
#         instance = super().__new__(cls)
#         instance.value = value
#         return instance

#     def __setattr__(self, key, value):
#         if key != "value":  # Allow setting 'value', but not other attributes
#             raise AttributeError(f"Cannot modify attribute '{key}', object is semi-immutable")
#         super().__setattr__(key, value)  # Actually set the value for 'value' attribute

# obj = SemiImmutableClass(10)
# print(obj.value)  # 10

# # The following will work because 'value' is allowed to be modified
# obj.value = 20
# print(obj.value)  # 20

# # This will raise an error because other attributes can't be modified
# # obj.other_attr = 30  # AttributeError: Cannot modify attribute 'other_attr', object is semi-immutable


# x = "global"

# def outer():
#     x = "enclosing"
    
#     def inner():
#         x = "local"
#         print(x)  # Will print "local" because Python finds `x` in the local scope first.

#     inner()
#     print(x)  # Will print "enclosing"

# outer()
# print(x)  # Will print "global"


# class PlayerCharacter:
#     def __init__(self, name):
#         self.name = name

#     def run(self, verb):
#         print(f'run {verb}')

#     @classmethod
#     def adding_things(cls, num1, num2):
#         return num1 + num2
   
# player1 =PlayerCharacter("Cindy")
# player2 =PlayerCharacter("Molly")

# #accessing class method using instance object
# print(player1.adding_things(2,5))  #output: 7

# ##Good practice: accessing class method using class name
# print(PlayerCharacter.adding_things(5,7))

# print(player1.run("fast")) # output = run fast



# player3= PlayerCharacter.adding_things(5,7)

 # def adding_things(cls, num1, num2):
    #     return cls("teddy",num1 + num2)




# txt = "apple#banana#cherry#orange"

# x = txt.split("#") 

# print(type(x)) #<class 'list'>
# print(x[2])     #cherry
# print(txt.split("#")[1])    #banana
# print(["apple", "banana", "cherry","orange"][3])    #orange

# class Product:
#     def __init__(self, name, price):
#         if price < 0:
#             raise ValueError("Price cannot be negative!")
#         self.name = name
#         self.price = price

#     @classmethod
#     def create(cls, name, price):
#         price = max(price, 0)  # Ensures price is never negative
#         return cls(name, price)

# p1 = Product.create("Laptop", -1000)  # Price auto-corrected to 0
# print(p1.name, p1.price)  # output: Laptop 0

# p2 =Product("phone", -2)

# class PlayerCharacter:
#     def __init__(self, name):
#         self.name = name

#     def run(self):
#         return self
    
# player1 =PlayerCharacter("Kath")
    

# #print (PlayerCharacter.run()) #TypeError: PlayerCharacter.run() missing 1 required positional argument: 'self'

# print (PlayerCharacter.run) #returns the method itself as a function reference, without calling it.
# print (PlayerCharacter.run(player1))
# print (player1)
# print (player1.run())

# class Employee:
#     def __init__(self, salary):
#         self.__salary = salary  # Private attribute

#     def get_salary(self):  # Getter method
#         return self.__salary

#     def set_salary(self, new_salary):  # Setter method
#         if new_salary > 0:
#             self.__salary = new_salary
#         else:
#             print("Invalid salary!")

# emp = Employee(5000)
# print(emp.get_salary())  # ✅ Access via getter

# emp.set_salary(6000)  # ✅ Modify via setter
# print(emp.get_salary())

# emp.set_salary(-1000)  # ❌ Invalid salary!

# print(emp.__salary) # AttributeError: 'Employee' object has no attribute '__salary'

# def custom_decorator(func):
#     def wrapper(*args, **kwargs):
#         print("Custom behavior before calling the function")
#         return func(*args, **kwargs)
#     return wrapper

# class Example:
#     @custom_decorator
#     def say_hello(self):
#         print("Hello!")

# e = Example() # Custom behavior before calling the function
# e.say_hello() # Hello!


# class Car:
#     def __init__(self, model):
#         self.model = model  # Public instance attribute

#     def __private_method(self):  # Private method
#         return f"Accessing public attribute: {self.model}"

#     def access_private_method(self):  # Public method calling private method
#         return self.__private_method()

# car = Car("Toyota")
# print(car.access_private_method())   #Accessing public attribute: Toyota

#Public method type is dynamically changed
# car.access_private_method= 9
# print(car.access_private_method) #output =9

# print(car.access_private_method()) # TypeError: 'int' object is not callable

# print(car.__private_method = 10) #changing is not allowed

#print(car.__private_method()) # AttributeError: 'Car' object has no attribute '__private_method'

# class Parent1:
#     def function1(self):
#         print("parent1 function executed")
#         return "return from function from Parent1"

# class Parent2:
#     def function1(self):
#         print("parent2 function executed")
#         return "return from function from Parent2"

# class Child(Parent2, Parent1):
#     def function2(self):
#         print("child class function executed")
#         return "return from function from Child"

# child = Child()
# print(child.function1())  
# print(child.function2())  

#print(Child.__mro__) #(<class '__main__.Child'>, <class '__main__.Parent1'>, 
                     #<class '__main__.Parent2'>, <class 'object'>)



# class A:
#     def speak(self):
#         print("speak method from A")
#         return "Method from A"

# class B:
#     def speak(self):
#         print("speak method frm B")
#         return "Method from B"

# class C(A, B):
#     def speak(self):
#         print("speak method from C")
#         return super().speak() + " and  Method from class C is also called" # Call the next class's speak() in MRO

# c = C()
# print(c.speak())  # This will use super() to call the method from class A.

# class A:
#     def speak(self):
#         return "A's speak method"

# class B(A):
#     def speak(self):
#         return "B's speak method"

# class C(A):
#     def speak(self):
#         return "C's speak method"

# class D(B, C):  # D inherits from both B and C
#     def speak(self):
#         return super().speak()  # Calls the speak method from parent classes (B and C)
    
# print(D.mro())
# #[<class '__main__.D'>, <class '__main__.B'>, <class '__main__.C'>, <class '__main__.A'>, <class 'object'>]




# class A:
#     def speak(self):
#         return "A's speak method"

# class B:
#     pass

# class D:
#     def speak(self):
#         return "D's speak method"

# class C(A, B, D):  # C inherits from A, B, and D
#     def speak(self):
#         return super(A, self).speak() #Skips class A and move to class B

# c = C()
# print(c.speak())  # Which method is called?  Ans: D's speak method





# class A:
#     def speak(self):
#         return "A's method"

# class B:
#     def speak(self):
#         return "B's method"

# class C(A, B):  # Inherits from A and B
#     def speak(self):
#         return super(A, self).speak()  # Explicitly calls the method from B, not A

# c = C()
# print(c.speak())  # This will access B's speak() instead of A's.




# class A:
#     def speak(self):
#         print("Inside A.speak() - START")
#         return "Method from A"

# class B:
#     def speak(self):
#         print("Inside B.speak() - START")
#         return "Method from B"

# class C(A, B):
#     def speak(self):
#         print("Inside C.speak() - START")  # ✅ This runs first
        
#         x = 42  # Variable initialization ✅ This runs
#         print("C is doing some work...")  # ✅ This runs

#         print("Calling super().speak()...")  # ✅ This runs
#         #result = super().speak()  # 🔥 Control moves to next method in MRO (A.speak)
        
#         print("Back in C.speak() after super()!")  # ✅ This runs after A.speak() finishes

#         return super().speak()+ " and Method from class C is also called"

# # Creating an instance of C
# c = C()

# # Calling speak() method
# print(c.speak())




# class Animal:
#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return "Animal makes a sound"

# class Dog(Animal):
#     def speak(self):
#         print ("Dog initialized")

#         result = super().speak()

#         dog_list = [1,2,3,4,5]
#         for dog in dog_list:
#             print(dog, end = " ")

#         print() #next line

#          # Calls the parent class method
#         return  result + " and Dog make a sound" 

# dog = Dog("Buddy")
# print(dog.speak())  




#Parent class
# class Animal:
#     def __init__(self, name, species):
#         self.name = name  # Parent class attribute
#         self.species = species  # Parent class attribute
    
#     def make_sound(self):  # Parent class method
#         print("Some generic animal sound")
    
#     def introduce(self):  # Parent class method
#         print(f"I am {self.name}, a {self.species}")

# # Child class inheriting from Animal
# class Dog(Animal):
#     def __init__(self, name, breed):
#         # Calling parent class's __init__ to set name and species
#         # super().__init__(name, species="Dog")   # calling parent attribute using super or
#         Animal.__init__(self,name, species="Dog")  # using class name
#         self.breed = breed  # Child class's own attribute
    
#     # Overriding parent class method
#     def make_sound(self):
#         print("Woof! Woof!")
    
#     def show_info(self):
#         # Using parent class's attribute (name) and method (introduce)
#         print(f"My name is {self.name}")  # Accessing parent attribute
#         self.introduce()  # Calling parent method
#         print(f"I'm a {self.breed} breed")

# # Creating an instance of Dog
# my_dog = Dog("Buddy", "Golden Retriever")

# # Using methods (some inherited, some overridden, some new)
# my_dog.make_sound()  # Calls Dog's version (overridden)
# my_dog.introduce()   # Calls Animal's version (inherited)
# my_dog.show_info()   # Calls Dog's new method that uses parent's attributes/methods

# # Accessing attributes (some inherited, some new)
# print(f"Species: {my_dog.species}")  # Inherited from Animal
# print(f"Breed: {my_dog.breed}")      # Specific to Dog






# # First Parent Class
# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand  # First parent attribute
#         self.model = model  # First parent attribute
    
#     def show_vehicle_info(self):  # First parent method
#         print(f"Vehicle: {self.brand} {self.model}")

# # Second Parent Class
# class ElectricDevice:
#     def __init__(self, battery_capacity):
#         self.battery_capacity = battery_capacity  # Second parent attribute
#         self.is_charging = False  # Second parent attribute
    
#     def charge(self):  # Second parent method
#         self.is_charging = True
#         print(f"Charging the device with {self.battery_capacity}kWh battery")

# # Child Class inheriting from both Vehicle and ElectricDevice
# class ElectricCar(Vehicle, ElectricDevice):
#     def __init__(self, brand, model, battery_capacity, range_per_charge):
#         # Initialize first parent (Vehicle)
#         Vehicle.__init__(self, brand, model)
#         # Initialize second parent (ElectricDevice)
#         ElectricDevice.__init__(self, battery_capacity)
#         # Child's own attribute
#         self.range_per_charge = range_per_charge
    
#     def show_info(self):  # Child's method using parent attributes
#         # Using Vehicle's method
#         self.show_vehicle_info()
#         # Using ElectricDevice's attribute
#         print(f"Battery: {self.battery_capacity}kWh")
#         # Using Vehicle's attribute
#         print(f"Model: {self.model}")
#         # Using child's own attribute
#         print(f"Range: {self.range_per_charge} miles")
        
#     def start_charging(self):  # Using parent's method with extension
#         print("Preparing electric car for charging...")
#         # Using ElectricDevice's method
#         self.charge()
#         print("Charging process started!")

# # Creating an instance
# my_tesla = ElectricCar("Tesla", "Model S", 100, 370)

# # Using methods and attributes from both parents and child
# my_tesla.show_info()
# print("\n")
# my_tesla.start_charging()

# # Accessing attributes from all levels
# print(f"\nIs charging? {my_tesla.is_charging}")  # From ElectricDevice
# print(f"Brand: {my_tesla.brand}")  # From Vehicle


# # A proper mixin (meaningless alone)
# class FlightMixin:
#     def take_off(self):
#         print(f"{self.name} is taking off!")
    
#     def land(self):
#         print(f"{self.name} is landing!")

# # ❌ Bad Usage: Instantiating the mixin directly
# flight = FlightMixin()
# flight.take_off()  # CRASH! AttributeError: 'name' doesn't exist



# class Person:
#     def __init__(self, name):
#         print("Person init")
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, emp_id):
#         print("Employee init")
#         super().__init__(name)
#         self.emp_id = emp_id

# class Customer(Person):
#     def __init__(self, name, balance):
#         print("Customer init")
#         super().__init__(name)
#         self.balance = balance

# # # Diamond inheritance(will cause error):
# # class EmployeeCustomer(Employee, Customer):
# #     def __init__(self, name, emp_id, balance):
# #         print("EmployeeCustomer init")
# #         super().__init__(name, emp_id)  # How to handle balance?!

# # ec = EmployeeCustomer("Alice", "E123", 100.50)

#Solution1 but error again
# class EmployeeCustomer(Employee, Customer):
#     def __init__(self, name, emp_id, balance):
#         # First initialize Employee branch
#         super().__init__(name, emp_id)
        
#         # Then manually initialize Customer branch
#         super(Employee, self).__init__(name, balance)

#         print("EmployeeCustomer fully initialized")

# ec = EmployeeCustomer("Alice", "E123", 100.50)



# class Person:
#     def __init__(self, name, **kwargs):
#         print(f"Person init: {name}")
#         self.name = name

# class Employee(Person):
#     def __init__(self,  emp_id, **kwargs):
#         print(f"Employee init:  {emp_id}")
#         super().__init__(**kwargs)
#         print("returning to initialize emp_id") 
#         self.emp_id = emp_id

# class Customer(Person):
#     def __init__(self, balance, **kwargs):
#         print(f"Customer init:  {balance}")
#         super().__init__( **kwargs)
#         print("returning to initialize balance") 
#         self.balance = balance

# class EmployeeCustomer(Employee, Customer):
#     def __init__(self, name, emp_id, balance):
#         print(f"EmployeeCustomer init")
#         super().__init__(name=name, emp_id=emp_id, balance=balance)
#         print("returning to Child class") 

# ec = EmployeeCustomer("Alice", "E123", 100.50)



# class Person:
#     def __init__(self, name, **kwargs):
#         print(f"Person setting name: {name}")
#         self.name = name

# class Employee(Person):
#     def __init__(self, emp_id, **kwargs):
#         print(f"Employee about to call super()")
#         super().__init__(**kwargs)
#         print(f"Employee setting emp_id: {emp_id}")
#         self.emp_id = emp_id  # This DOES execute!

# ec = Employee(name ="Alice", emp_id ="E123")

# print(isinstance(ec, Person)) #True
# print(isinstance(ec, object)) #True




# class Person:
#     def __init__(self, name, **kwargs):
#         print(f"Person init: {name}")
#         self.name = name

# class Employee(Person):
#     def __init__(self, name, emp_id, **kwargs):
#         print(f"Employee init: {name}, {emp_id}")
#         super().__init__(name, **kwargs)
#         self.emp_id = emp_id

# class Customer(Person):
#     def __init__(self, name, balance, **kwargs):
#         print(f"Customer init: {name}, {balance}")
#         super().__init__(name, **kwargs)
#         self.balance = balance

# class EmployeeCustomer(Employee, Customer):
#     def __init__(self, name, emp_id, balance):
#         print(f"EmployeeCustomer init")
#         super().__init__(name=name, emp_id=emp_id, balance=balance)

# ec = EmployeeCustomer("Alice", "E123", 100.50)

# print(EmployeeCustomer.__mro__)#(<class '__main__.EmployeeCustomer'>, 
# #<class '__main__.Employee'>, <class '__main__.Customer'>, <class '__main__.Person'>, 
# #<class 'object'>)


# class FrontDesk:
#     def process(self):
#         print("Front Desk: Document logged")

# class DepartmentHead(FrontDesk):
#     def process(self):
#         super().process()  # Calls FrontDesk
#         print("Department Head: Verification done")

# class AuditMixin:
#     def process(self):
#         print("AuditMixin: Bypassing Department Head!")
#         super(DepartmentHead, self).process()  # Skips DepartmentHead → FrontDesk

# class CEO(AuditMixin, DepartmentHead):
#     def process(self):
#         super().process()  # Normally goes to DepartmentHead, but mixin redirects
#         print("CEO: Final approval given")

# # Run the process
# approval_flow = CEO()
# approval_flow.process()
# print(CEO.__mro__)
# #(<class '__main__.CEO'>, <class '__main__.AuditMixin'>, <class '__main__.DepartmentHead'>,
# #  <class '__main__.FrontDesk'>, <class 'object'>)


# class Parent:
#     def __init__(self, name):
#         self.name = name
#         print(f"Parent initialized: {self.name}")

#     def greet(self):
#         print(f"Hello from {self.name}")

# # Child 1
# class Child1(Parent):
#     def __init__(self, name, feature):
#         super().__init__(name)  # Initialize Parent
#         self.feature = feature
#         print(f"Child1 added: {self.feature}")

# # Child 2
# class Child2(Parent):
#     def __init__(self, name, tool):
#         super().__init__(name)  # Initialize Parent
#         self.tool = tool
#         print(f"Child2 added: {self.tool}")

# # Usage
# dog = Child1("Buddy", "Barking") #output: Parent initialized: Buddy, Child1 added: Barking
# cat = Child2("Whiskers", "Purring") #ouput:Parent initialized: Whiskers, Child2 added: Purring

# dog.greet()  # Inherited from Parent,  Output : Hello from Buddy
# cat.greet()  # Inherited from Parent,  Output: Hello from Whiskers
# print(Child1.__mro__)  # Output: (Child1, Parent, object)

# class Weapon:
#     def attack(self):
#         return "Weapon attack"

# class Character:
#     def __init__(self, name, weapon):
#         self.name = name
#         self.weapon = weapon

#     def attack(self):
#         return f"{self.name} attacks with {self.weapon.attack()}"

# sword = Weapon()
# warrior = Character("Warrior", sword)
# print(warrior.attack())  # Output: Warrior attacks with Weapon attack


# class Logger:
#     def log(self, message):
#         print(f"LOG: {message}")

# class Car:
#     def __init__(self):
#         self.logger = Logger()  # Composition

#     def drive(self):
#         self.logger.log("Car started driving")
#         print("Vroom!")

# class User:
#     def __init__(self, name):
#         self.name = name
#         self.logger = Logger()  # Composition

#     def greet(self):
#         self.logger.log(f"User {self.name} greeted")
#         print(f"Hello, {self.name}!")

# # Usage
# car = Car()
# car.drive()  # Output: LOG: Car started driving → Vroom!

# user = User("Alice")
# user.greet()  # Output: LOG: User Alice greeted → Hello, Alice!



# class LoggableMixin:
#     def log(self, message):
#         print(f"LOG: {message}")

# class Car(LoggableMixin):
#     def drive(self):
#         self.log("Car started driving")  # Direct access to log()
#         print("Vroom!")

# class User(LoggableMixin):
#     def __init__(self, name):
#         self.name = name

#     def greet(self):
#         self.log(f"User {self.name} greeted") # Direct access to log()
#         print(f"Hello, {self.name}!")

# # Usage
# car = Car()
# car.drive()  # Output: LOG: Car started driving → Vroom!

# user = User("Alice")
# user.greet()  # Output: LOG: User Alice greeted → Hello, Alice!



# class Animal:
#     def eat(self):
#         print("Eating...")

# class Mammal(Animal):  # Multilevel
#     def walk(self):
#         print("Walking")

# class Bird(Animal):  # Hierarchical
#     def fly(self):
#         print("Flying")

# class Dog(Mammal):  # Further specialization
#     def bark(self):
#         print("Woof!")

# class Parrot(Bird):
#     def chirp(self):
#         print("Chirp chirp!")

# # Usage
# dog = Dog()
# dog.eat()  # From Animal   Eating...
# dog.walk() # From Mammal   Walking
# dog.bark() # From Dog      Woof!  

# parrot = Parrot()
# parrot.fly()  # From Bird   Flying 


# class Base:
#     def show(self):
#         print("Base")

# class Child1(Base):
#     def show(self):
#         print("Child1")
#         super().show()

# class Child2(Base):
#     def show(self):
#         print("Child2")
#         super().show()

# class GrandChild(Child1, Child2):  # Multiple + Multilevel
#     def show(self):
#         print("GrandChild")
#         super().show()

# gc = GrandChild()
# gc.show()


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
#         print(f"Initialized {self.brand} {self.model}")

#     def start_engine(self):
#         print(f"{self.brand} engine started")

# class LandVehicle(Vehicle):  # Multilevel
#     def __init__(self, brand, model, wheels):
#         super().__init__(brand, model)
#         self.wheels = wheels

#     def drive(self):
#         print(f"Driving {self.wheels}-wheeled {self.brand}")

# class WaterVehicle(Vehicle):  # Hierarchical (sibling of LandVehicle)
#     def __init__(self, brand, model, buoyancy):
#         super().__init__(brand, model)
#         self.buoyancy = buoyancy

#     def float(self):
#         print(f"{self.brand} floating with buoyancy {self.buoyancy}")

# class Car(LandVehicle):  # Further specialization
#     def __init__(self, brand, model, wheels, fuel_type):
#         super().__init__(brand, model, wheels)
#         self.fuel_type = fuel_type

#     def refuel(self):
#         print(f"Refueling {self.brand} with {self.fuel_type}")

# class Boat(WaterVehicle):
#     def __init__(self, brand, model, buoyancy, max_speed):
#         super().__init__(brand, model, buoyancy)
#         self.max_speed = max_speed

#     def sail(self):
#         print(f"{self.brand} sailing at {self.max_speed} knots")

# # Usage
# tesla = Car("Tesla", "Model S", 4, "Electric") #Initialized Tesla Model S
# tesla.start_engine()  # From Vehicle,    Tesla engine started
# tesla.drive()        # From LandVehicle,     Driving 4-wheeled Tesla   
# tesla.refuel()       # From Car,     Refueling Tesla with Electric

# yacht = Boat("Yamaha", "242X", "High", 40) #Initialized Yamaha 242X
# yacht.float()        # From WaterVehicle,   Yamaha floating with buoyancy High
# yacht.sail()         # From Boat,      Yamaha sailing at 40 knots




# class PowerDevice:
#     def __init__(self, power_source):
#         self.power_source = power_source
#         print(f"Power source: {self.power_source}")

#     def power_on(self):
#         print(f"Powered by {self.power_source}")

# class NetworkDevice:
#     def __init__(self, ip_address):
#         self.ip_address = ip_address
#         print(f"IP: {self.ip_address}")

#     def connect(self):
#         print(f"Connected to network at {self.ip_address}")

# class SmartDevice(PowerDevice, NetworkDevice):  # Multiple inheritance
#     def __init__(self, power_source, ip_address, device_name):
#         PowerDevice.__init__(self, power_source)       # Explicit init for PowerDevice
#         NetworkDevice.__init__(self, ip_address)       # Explicit init for NetworkDevice
#         self.device_name = device_name

#     def status(self):
#         print(f"{self.device_name} status: OK")

# class SmartLight(SmartDevice):  # Multilevel
#     def __init__(self, power_source, ip_address, device_name, brightness):
#         super().__init__(power_source, ip_address, device_name)
#         self.brightness = brightness

#     def adjust_light(self, level):
#         self.brightness = level
#         print(f"Brightness set to {self.brightness}%")

# # Usage
# light = SmartLight("Battery", "192.168.1.100", "Living Room Light", 50) 
# light.power_on()    # From PowerDevice,  
# light.connect()     # From NetworkDevice
# light.status()      # From SmartDevice
# light.adjust_light(75)  # From SmartLight

# print(SmartLight.__mro__) #(<class '__main__.SmartLight'>, 
# #<class '__main__.SmartDevice'>, <class '__main__.PowerDevice'>, 
# # <class '__main__.NetworkDevice'>, <class 'object'>)



# class Dog:
#     def speak(self):
#         return "Woof!"

# class Cat:
#     def speak(self):
#         return "Meow!"

# def animal_sound(animal):
#     print(animal.speak())

# animal_sound(Dog())   # Woof!
# animal_sound(Cat())   # Meow!


# from abc import ABC, abstractmethod

# class Shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

# class Circle(Shape):
#     def __init__(self,r):
#          self.r = r

#     def area(self):
#         return 2* 3.14 * self.r 

# class Square(Shape):
#     def __init__(self,x,y):
#         self.x =x
#         self.y = y

#     def area(self):
#         return self.x * self.y

# shapes = [Circle(3), Square(2, 5)]

# for shape in shapes:
#     print(shape.area())  # Polymorphism in action

# class JSONExporter:
#     def export(self, data):
#         print(f"Exporting {data} as JSON")

# class XMLExporter:
#     def export(self, data):
#         print(f"Exporting {data} as XML")

# class DataPipeline:
#     def __init__(self, exporter):  # Loose coupling
#         self.exporter = exporter #the attribute will become the object

#     def run(self, data):
#         self.exporter.export(data) #use the attribute asn an object to call  
#                                   # method of other class

# # Switch exporters seamlessly
# pipeline = DataPipeline(JSONExporter())
# pipeline.run({"key": "value"})  # Output: Exporting {'key': 'value'} as JSON

# #pipeline.exporter - this one accessed the attribute and instantiated another class object
# pipeline.exporter = XMLExporter()  # Change behavior at runtime
# pipeline.run({"key": "value"})  # Output: Exporting {'key': 'value'} as XML


# import time
# from functools import wraps

# def log_execution(func):
#     @wraps(func)  # Preserves function metadata
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         print(f"Executing {func.__name__} with args: {args}, kwargs: {kwargs}")
        
#         result = func(*args, **kwargs)  # Call the original function
        
#         end_time = time.time()
#         print(f"Finished {func.__name__} in {end_time - start_time:.4f}s. Result: {result}")
#         return result
#     return wrapper

# @log_execution
# def calculate_sum(a, b):
#     time.sleep(1)  # Simulate slow computation
#     return a + b

# calculate_sum(3, b=4)



# # Without @wraps(func):
# print(calculate_sum.__name__)  # Output: 'wrapper' (oops!)
# print(calculate_sum.__doc__)   # Output: None (docstring lost!)


# import time
# from functools import wraps

# def retry_on_failure(max_retries=3, delay=1):
#     def decorator(func):
#         @wraps(func)
#         def wrapper(*args, **kwargs):
#             retries = 0
#             while retries < max_retries:
#                 try:
#                     return func(*args, **kwargs)
#                 except Exception as e:
#                     retries += 1
#                     print(f"Attempt {retries} failed: {e}. Retrying in {delay}s...")
#                     time.sleep(delay)
#             raise RuntimeError(f"Failed after {max_retries} retries")
#         return wrapper
#     return decorator

# @retry_on_failure(max_retries=2, delay=0.5)
# def fetch_data(url):
#     # Simulate a flaky network request
#     import random
#     if random.random() < 0.7:  # 70% chance of failure
#         raise ConnectionError("Network error!")
#     return "Data fetched successfully"

# fetch_data("https://api.example.com")



# Manual equivalent of @retry_on_failure(max_retries=2, delay=0.5)
# def fetch_data(url):
#     pass

# # Step 1: Configure the decorator
# configured_decorator = retry_on_failure(max_retries=2, delay=0.5)

# # Step 2: Apply to the function
# fetch_data = configured_decorator(fetch_data)


# def add_class_methods(*methods):
#     def decorator(cls):
#         for method_name, method in methods:
#             setattr(cls, method_name, method)  # Inject methods into the class
#         return cls
#     return decorator

# # Define methods to inject
# def greet(self):
#     return f"Hello from {self.__class__.__name__}!"

# def farewell(self):
#     return "Goodbye!"

# #passing method name and method as argument
# @add_class_methods(("greet", greet),("farewell", farewell))
# class MyClass:
#     pass

# obj = MyClass()
# print(obj.greet())    # Output: Hello from MyClass!  
# print(obj.farewell()) # Output: Goodbye!  


# from functools import singledispatch

# @singledispatch
# def process(data):
#     """Base implementation for unknown types"""
#     print(f"Processing unknown data: {data}")

# @process.register(str)
# def _(text):
#     """Handle string input"""
#     print(f"Processing text: {text.upper()}")

# @process.register(int)
# def _(number):
#     """Handle integer input"""
#     print(f"Processing number: {number * 2}")

# @process.register(list)
# def _(items):
#     """Handle list input"""
#     print(f"Processing list: {len(items)} items")

# # Testing the function
# process("hello")    # Output: Processing text: HELLO
# process(42)         # Output: Processing number: 84
# process([1, 2, 3])  # Output: Processing list: 3 items
# process(3.14)       # Output: Processing unknown data: 3.14


# #Advanced Usage
# #Working with Custom Classes
# class User:
#     def __init__(self, name):
#         self.name = name

# @process.register(User)
# def _(user):
#     print(f"Processing user: {user.name}")

# process(User("Alice"))  # Output: Processing user: Alice


# class Animal:
#     species = "mammal"

#     def __init__(self, name):
#         self.name = name

#     def speak(self):
#         return f"{self.name} makes a sound"
# a = Animal("Tiger")
# print(dir(a))

# class Person:
#     __slots__ = ['name', 'age']

#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

# p = Person("Alice", 30)
# print(p.name)  # ✅ works # Alice
# print(p.age)   # ✅ works # 30

# #✅ Step-by-step Implementation Using Introspection
# class Serializer:
#     def serialize(self, obj):
#         if not hasattr(obj, '__dict__'):
#             raise ValueError("Cannot serialize this object")

#         data = {}
#         for attr, value in vars(obj).items():
#             if not attr.startswith("_"):  # Ignore private/internal
#                 data[attr] = value
#         return data

# #📦 Example Classes to Serialize
# class User:
#     def __init__(self, username, email, is_admin=False):
#         self.username = username
#         self.email = email
#         self.is_admin = is_admin
#         self._internal_id = 123  # Should not be serialized

# class Product:
#     def __init__(self, name, price):
#         self.name = name
#         self.price = price


# #🚀 Using the Serializer
# s = Serializer()

# user = User("alice", "alice@example.com", True)
# product = Product("Laptop", 1200)

# print(s.serialize(user))
# # Output: {'username': 'alice', 'email': 'alice@example.com', 'is_admin': True}

# print(s.serialize(product))
# # Output: {'name': 'Laptop', 'price': 1200}

# import inspect
# from collections import defaultdict

# class Employee:
#     """A class representing an employee"""
    
#     company = "TechCorp"
    
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary
    
#     def get_info(self):
#         """Returns employee information"""
#         return f"{self.name} earns ${self.salary:,} at {self.company}"
    
#     @classmethod
#     def from_dict(cls, data):
#         """Alternative constructor from dictionary"""
#         return cls(data['name'], data['salary'])
    
#     @staticmethod
#     def calculate_bonus(salary, percentage):
#         """Calculates bonus amount"""
#         return salary * percentage / 100

# def process_data(data: dict, verbose: bool = False) -> list:
#     """Processes employee data with optional verbosity"""
#     results = []
#     for emp in data.get('employees', []):
#         e = Employee.from_dict(emp)
#         results.append(e.get_info())
#         if verbose:
#             print(f"Processed: {e.name}")
#     return results

# # Get all members of Employee class
# members = inspect.getmembers(Employee)

# print(f"members type: {type(members)}") #return type of inspect.getmembers()
# #print(members) # list of tuples

# # Filter out dunder methods
# clean_members = [(name, obj) for name, obj in members 
#                 if not name.startswith('__')]

# print(f"clean_members type: {type(clean_members)}")
# #print(clean_members) #list of tuples

# print("Employee class members:")
# for name, obj in clean_members:
#     print(f"{name}: {type(obj).__name__}")


# sig = inspect.signature(process_data)
# print("\nFunction signature:")
# print(sig)

# print("\nParameter details:")
# for name, param in sig.parameters.items():
#     print(f"{name}:")
#     print(f"  kind: {param.kind}")
#     print(f"  default: {param.default}")
#     print(f"  annotation: {param.annotation}")

# print("\nSource code of process_data:")
# print(inspect.getsource(process_data))

# print("\nMethod Resolution Order:")
# print(inspect.getmro(Employee))

# print("\nType checks:")
# print(f"Is Employee a class? {inspect.isclass(Employee)}")
# print(f"Is get_info a method? {inspect.ismethod(Employee.get_info)}")
# print(f"Is from_dict a classmethod? {inspect.ismethod(Employee.from_dict)}")
# print(f"Is calculate_bonus static? {inspect.isfunction(Employee.calculate_bonus)}")

# import inspect

# def function_a():
#     function_b()

# def function_b():
#     current_stack = inspect.stack()
#     print("\nCurrent call stack:")
#     for frame_info in current_stack:
#         print(f"{frame_info.function} in {frame_info.filename}:{frame_info.lineno}")

# function_a()

# import inspect

# def analyze_frame():
#     frame = inspect.currentframe()
#     print("\nFrame information:")
#     print(f"Function name: {frame.f_code.co_name}")
#     print(f"Line number: {frame.f_lineno}")
#     print(f"Local variables: {frame.f_locals.keys()}")

# def test_function(x, y=10):
#     z = x + y
#     analyze_frame()
#     return z

# test_function(5)

# import inspect

# def explore(obj, depth=0, max_depth=2):
#     """Recursively explore an object's structure"""
#     if depth > max_depth:
#         return
    
#     indent = '  ' * depth
#     print(f"\n{indent}Exploring: {type(obj).__name__}")
    
#     # Get all non-dunder members
#     members = inspect.getmembers(obj, lambda x: not inspect.isroutine(x))
#     members = [(name, val) for name, val in members 
#               if not name.startswith('__')]
    
#     for name, val in members:
#         print(f"{indent}{name}: {type(val).__name__}")
#         if inspect.isclass(val) or inspect.ismodule(val):
#             explore(val, depth+1, max_depth)

# # Explore the Employee class
# explore(Employee)

# class Book:
#     def __new__(cls, *args, **kwargs):
#         print("__new__ - Creating instance")
#         instance = super().__new__(cls)
#         return instance
    
#     def __init__(self, title, author, pages):
#         print("__init__ - Initializing instance")
#         self.title = title
#         self.author = author
#         self.pages = pages
    
#     def __del__(self):
#         print(f"__del__ - Deleting book: {self.title}")
    
#     def __repr__(self):
#         return f"Book({self.title!r}, {self.author!r}, {self.pages})"
    
#     def __str__(self):
#         return f"'{self.title}' by {self.author}, {self.pages} pages"
    
#     def __format__(self, format_spec):
#         if format_spec == 'short':
#             return f"{self.title} ({self.author})"
#         elif format_spec == 'long':
#             return f"Book: {self.title}\nAuthor: {self.author}\nPages: {self.pages}"
#         return str(self)
    
#     def __bytes__(self):
#         import json
#         data = {'title': self.title, 'author': self.author, 'pages': self.pages}
#         return json.dumps(data).encode('utf-8')

# # Demonstration
# if __name__ == "__main__":
#     # __new__ and __init__ get called here
#     book = Book("Python Tricks", "Dan Bader", 302)
    
#     print("\n__repr__ output:")
#     print(repr(book))  # Book('Python Tricks', 'Dan Bader', 302)
    
#     print("\n__str__ output:")
#     print(str(book))   # 'Python Tricks' by Dan Bader, 302 pages
#     print(book)        # same as above (print calls __str__)
    
#     print("\n__format__ outputs:")
#     print(f"{book:short}")  # Python Tricks (Dan Bader)
#     print(f"{book:long}")
#     # Book: Python Tricks
#     # Author: Dan Bader
#     # Pages: 302
    
#     print("\n__bytes__ output:")
#     print(bytes(book))  # b'{"title": "Python Tricks", "author": "Dan Bader", "pages": 302}'
    
#     # __del__ gets called when object is deleted or program ends
#     del book



# class BankAccount:
#     def __init__(self, account_holder, balance):
#         self.holder = account_holder
#         self.balance = balance
    
#     # Comparison methods
#     def __eq__(self, other):
#         """Equal to (==) - same balance"""
#         if not isinstance(other, BankAccount):
#             return NotImplemented
#         return self.balance == other.balance
    
#     def __ne__(self, other):
#         """Not equal to (!=) - delegates to __eq__"""
#         return not (self == other)
    
#     def __lt__(self, other):
#         """Less than (<) - compares balances"""
#         if not isinstance(other, BankAccount):
#             return NotImplemented
#         return self.balance < other.balance
    
#     def __le__(self, other):
#         """Less than or equal (<=) - compares balances"""
#         if not isinstance(other, BankAccount):
#             return NotImplemented
#         return self.balance <= other.balance
    
#     def __gt__(self, other):
#         """Greater than (>) - compares balances"""
#         if not isinstance(other, BankAccount):
#             return NotImplemented
#         return self.balance > other.balance
    
#     def __ge__(self, other):
#         """Greater than or equal (>=) - compares balances"""
#         if not isinstance(other, BankAccount):
#             return NotImplemented
#         return self.balance >= other.balance
    
#     def __str__(self):
#         return f"{self.holder}'s account: ${self.balance:.2f}"

# # Demonstration
# if __name__ == "__main__":
#     alice = BankAccount("Alice", 1000)
#     bob = BankAccount("Bob", 1500)
#     charlie = BankAccount("Charlie", 1000)
    
#     print(f"{alice}\n{bob}\n{charlie}\n")
    
#     # __eq__ and __ne__
#     print("Equality tests:")
#     print(f"Alice == Charlie: {alice == charlie}")  # True (same balance)
#     print(f"Alice != Bob: {alice != bob}")          # True
    
#     # __lt__ and __gt__
#     print("\nRelative comparisons:")
#     print(f"Alice < Bob: {alice < bob}")            # True
#     print(f"Bob > Alice: {bob > alice}")            # True
    
#     #__le__ and __ge__
#     print("\nLess/Greater or equal:")
#     print(f"Alice <= Charlie: {alice <= charlie}")   # True
#     print(f"Alice >= Charlie: {alice >= charlie}")   # True
#     print(f"Alice <= Bob: {alice <= bob}")          # True
#     print(f"Bob >= Charlie: {bob >= charlie}")      # True


# class Vector:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Arithmetic Operations
#     def __add__(self, other):          # + (vector addition)
#         if isinstance(other, Vector):
#             return Vector(self.x + other.x, self.y + other.y)
#         return NotImplemented

#     def __sub__(self, other):          # - (vector subtraction)
#         if isinstance(other, Vector):
#             return Vector(self.x - other.x, self.y - other.y)
#         return NotImplemented

#     def __mul__(self, scalar):         # * (scalar multiplication)
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x * scalar, self.y * scalar)
#         return NotImplemented

#     def __truediv__(self, scalar):     # / (scalar division)
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x / scalar, self.y / scalar)
#         return NotImplemented

#     def __floordiv__(self, scalar):    # // (scalar floor division)
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x // scalar, self.y // scalar)
#         return NotImplemented

#     def __mod__(self, scalar):         # % (scalar modulus)
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x % scalar, self.y % scalar)
#         return NotImplemented

#     def __pow__(self, scalar):         # ** (scalar exponentiation)
#         if isinstance(scalar, (int, float)):
#             return Vector(self.x ** scalar, self.y ** scalar)
#         return NotImplemented

#     # In-Place Arithmetic (modifies self)
#     def __iadd__(self, other):         # += (in-place addition)
#         if isinstance(other, Vector):
#             self.x += other.x
#             self.y += other.y
#             return self
#         return NotImplemented

#     def __isub__(self, other):         # -= (in-place subtraction)
#         if isinstance(other, Vector):
#             self.x -= other.x
#             self.y -= other.y
#             return self
#         return NotImplemented

#     def __imul__(self, scalar):        # *= (in-place scalar mult.)
#         if isinstance(scalar, (int, float)):
#             self.x *= scalar
#             self.y *= scalar
#             return self
#         return NotImplemented

#     def __itruediv__(self, scalar):    # /= (in-place scalar division)
#         if isinstance(scalar, (int, float)):
#             self.x /= scalar
#             self.y /= scalar
#             return self
#         return NotImplemented

#     # String representation for printing
#     def __repr__(self):
#         return f"Vector({self.x}, {self.y})"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     v1 = Vector(3, 4)
#     v2 = Vector(2, 1)

#     print("Standard Arithmetic:")
#     print(f"v1 + v2 = {v1 + v2}")      # Vector(5, 5)
#     print(f"v1 - v2 = {v1 - v2}")      # Vector(1, 3)
#     print(f"v1 * 2 = {v1 * 2}")        # Vector(6, 8)
#     print(f"v1 / 2 = {v1 / 2}")        # Vector(1.5, 2.0)
#     print(f"v1 // 2 = {v1 // 2}")      # Vector(1, 2)
#     print(f"v1 % 2 = {v1 % 2}")        # Vector(1, 0)
#     print(f"v1 ** 2 = {v1 ** 2}")      # Vector(9, 16)

#     print("\nIn-Place Arithmetic:")
#     v1 += v2                           # v1 becomes Vector(5, 5)
#     print(f"v1 += v2 → {v1}")
#     v1 *= 2                            # v1 becomes Vector(10, 10)
#     print(f"v1 *= 2 → {v1}")


# class Temperature:
#     def __init__(self, celsius):
#         self.celsius = celsius
    
#     # Type Conversion Methods
#     def __int__(self):
#         """int(temperature) → truncates Celsius value"""
#         return int(self.celsius)
    
#     def __float__(self):
#         """float(temperature) → exact Celsius value"""
#         return float(self.celsius)
    
#     def __bool__(self):
#         """bool(temperature) → False only at absolute zero (-273.15°C)"""
#         return self.celsius > -273.15
    
#     def __complex__(self):
#         """complex(temperature) → Celsius as real part, Fahrenheit as imaginary"""
#         return complex(self.celsius, self.fahrenheit)
    
#     # Helper property for __complex__
#     @property
#     def fahrenheit(self):
#         return (self.celsius * 9/5) + 32
    
#     # String representation
#     def __repr__(self):
#         return f"Temperature({self.celsius}°C)"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     temp = Temperature(25.7)  # 25.7°C
    
#     print("Type Conversions:")
#     print(f"int(temp)    → {int(temp)}")        # 25 (truncated)
#     print(f"float(temp)  → {float(temp)}")      # 25.7 (exact)
#     print(f"bool(temp)   → {bool(temp)}")       # True (not absolute zero)
#     print(f"complex(temp)→ {complex(temp)}")    # (25.7+78.26j)
    
#     print("\nEdge Cases:")
#     absolute_zero = Temperature(-273.15)
#     print(f"bool(absolute_zero) → {bool(absolute_zero)}")  # False


# class Playlist:
#     def __init__(self, songs=None):
#         self.songs = list(songs) if songs else []
    
#     # Container Methods
#     def __len__(self):
#         """len(playlist) → number of songs"""
#         return len(self.songs)
    
#     def __getitem__(self, index):
#         """playlist[index] → get song by position or slice"""
#         return self.songs[index]
    
#     def __setitem__(self, index, song):
#         """playlist[index] = song → change song at position"""
#         self.songs[index] = song
    
#     def __delitem__(self, index):
#         """del playlist[index] → remove song at position"""
#         del self.songs[index]
    
#     def __contains__(self, song):
#         """song in playlist → check if song exists"""
#         return song in self.songs
    
#     def __iter__(self):
#         """for song in playlist → iterate through songs"""
#         return iter(self.songs)
    
#     def __reversed__(self):
#         """reversed(playlist) → iterate backwards"""
#         return reversed(self.songs)
    
#     # Bonus: Nice string representation
#     def __str__(self):
#         return "\n".join(f"{i+1}. {song}" for i, song in enumerate(self.songs))

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     pl = Playlist(["Blinding Lights", "Save Your Tears", "Take My Breath"])
    
#     print("Initial Playlist:")
#     print(pl)  # Uses __str__
    
#     print("\nContainer Operations:")
#     print(f"Number of songs (__len__): {len(pl)}")  # 3
#     print(f"First song (__getitem__): {pl[0]}")      # Blinding Lights
#     print(f"'Hello' in playlist? (__contains__): {'Hello' in pl}")  # False
    
#     pl[1] = "Starboy"  # __setitem__
#     del pl[2]          # __delitem__
    
#     print("\nModified Playlist:")
#     print(pl)
    
#     print("\nIteration:")
#     print("Forward (__iter__):", ", ".join(pl))
#     print("Backward (__reversed__):", ", ".join(reversed(pl)))

# import time

# class Timer:
#     def __init__(self, name="Timer"):
#         # Initialize timer with a name (default: "Timer")
#         self.name = name
#         self.start_time = None  # Will store when timer starts
#         self.end_time = None    # Will store when timer ends
    
#     # Context Manager Protocol Methods
#     def __enter__(self):
#         """Called when entering 'with' block"""
#         # 1. Record start time using high-precision counter
#         self.start_time = time.perf_counter()
#         # 2. Optional: Print status message
#         print(f"{self.name} started")
#         # 3. Return self to allow access to timer object in 'with...as'
#         return self
    
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         """Called when exiting 'with' block"""
#         # 1. Record end time
#         self.end_time = time.perf_counter()
#         # 2. Calculate elapsed time
#         elapsed = self.end_time - self.start_time
#         # 3. Print results
#         print(f"{self.name} finished in {elapsed:.4f} seconds")
        
#         # 4. Exception handling (all 3 parameters are None if no exception occurred)
#         if exc_type is not None:
#             print(f"⚠️ Exception occurred: {exc_val}")
#         # 5. Return False to let exceptions propagate up, True to suppress them
#         return False
    
#     # Bonus method for manual time checks
#     def elapsed(self):
#         """Returns current elapsed time if timer is running"""
#         return time.perf_counter() - self.start_time

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     print("=== Example 1: Basic Timing ===")
#     with Timer("Coffee Brew Timer"):
#         # Simulate work (summing numbers)
#         _ = sum(range(10_000_000))  # The underscore ignores the result
    
    # print("\n=== Example 2: Error Handling ===")
    # try:
    #     with Timer("Buggy Timer"):
    #         # This will fail halfway
    #         _ = sum(range(5_000_000))              #1. This will run
    #         raise ValueError("Artificial error!")  #2. This will force an error
    #         _ = sum(range(5_000_000))  # Never reached
    # except ValueError as e:
    #     print(f"Caught error outside: {repr(e)}")

    # print("\n=== Example 2: Intentional Error (Your Code) ===")
    # with Timer("Risky Operation") as t:
    #     x = 1 / 0  # Triggers ZeroDivisionError

    # # Note: This line won't run because the error crashes the program!
    # print("This message won't appear.")

# class Celsius:
#     """Descriptor for Celsius with automatic Fahrenheit conversion."""
#     def __get__(self, instance, owner):
#         """Called when getting the value: temp.celsius"""
#         return instance._celsius

#     def __set__(self, instance, value):
#         """Called when setting the value: temp.celsius = 25"""
#         instance._celsius = value
#         # Automatically update Fahrenheit
#         instance._fahrenheit = (value * 9/5) + 32

# class Temperature:
#     celsius = Celsius()  # Descriptor instance

#     def __init__(self, celsius):
#         self.celsius = celsius  # Triggers __set__

#     @property
#     def fahrenheit(self):
#         """Read-only Fahrenheit (managed by Celsius descriptor)"""
#         return self._fahrenheit

#     def __repr__(self):
#         return f"Temperature({self.celsius}°C, {self.fahrenheit}°F)"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     print("=== Descriptor in Action ===")
#     temp = Temperature(25)  # Initialized at 25°C
#     print(temp)  # Temperature(25°C, 77.0°F)

#     print("\nUpdating Celsius (triggers __set__):")
#     temp.celsius = 30  # Descriptor auto-updates Fahrenheit
#     print(temp)  # Temperature(30°C, 86.0°F)

#     print("\nAccessing Celsius (triggers __get__):")
#     print(f"It's {temp.celsius}°C outside!")  # 30


# class Vector2D:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     # Numeric Operations
#     def __abs__(self):
#         """Absolute value (magnitude) of the vector: abs(v)"""
#         return (self.x ** 2 + self.y ** 2) ** 0.5

#     def __neg__(self):
#         """Negation: -v"""
#         return Vector2D(-self.x, -self.y)

#     def __pos__(self):
#         """Unary plus: +v"""
#         return Vector2D(+self.x, +self.y)

#     def __invert__(self):
#         """Bitwise inversion (unary ~): ~v (rotates 90 degrees)"""
#         return Vector2D(-self.y, self.x)

#     def __round__(self, n=None):
#         """Rounding: round(v, 2)"""
#         return Vector2D(round(self.x, n), round(self.y, n))

#     def __trunc__(self):
#         """Truncation: math.trunc(v)"""
#         import math
#         return Vector2D(math.trunc(self.x), math.trunc(self.y))

#     def __floor__(self):
#         """Floor: math.floor(v)"""
#         import math
#         return Vector2D(math.floor(self.x), math.floor(self.y))

#     def __ceil__(self):
#         """Ceiling: math.ceil(v)"""
#         import math
#         return Vector2D(math.ceil(self.x), math.ceil(self.y))

#     def __repr__(self):
#         return f"Vector2D({self.x}, {self.y})"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     v = Vector2D(3.3, -4.4)

#     print("Original:", v)
#     print("Absolute value (magnitude):", abs(v))        # 5.5
#     print("Negated:", -v)                              # Vector2D(-3.3, 4.4)
#     print("Unary plus:", +v)                           # Vector2D(3.3, -4.4)
#     print("Bitwise inverted (~):", ~v)                 # Vector2D(4.4, 3.3)
#     print("Rounded (1 decimal):", round(v, 1))         # Vector2D(3.3, -4.4)
#     print("Truncated:", v.__trunc__())                 # Vector2D(3, -4)
#     print("Floored:", v.__floor__())                   # Vector2D(3, -5)
#     print("Ceiling:", v.__ceil__())                    # Vector2D(4, -4)

# class DynamicConfig:
#     def __init__(self):
#         # Stores actual attributes
#         self._data = {}

#     # Custom Attribute Access
#     def __getattr__(self, name):
#         """Called when an attribute is NOT found (default lookup fails)"""
#         if name in self._data:
#             return self._data[name]
#         raise AttributeError(f"'DynamicConfig' has no attribute '{name}'")

#     def __setattr__(self, name, value):
#         """Called for ALL attribute assignments"""
#         if name == '_data':  # Allow _data initialization
#             super().__setattr__(name, value)
#         else:
#             # Validate and store in _data dictionary
#             if not name.islower(): #islower() returns false if If there are no alphabetic
#                                    #characters, or if there's at least one uppercase letter
#                 raise ValueError("Attribute names must be lowercase!")
#             self._data[name] = f"VALIDATED_{value}"

#     def __delattr__(self, name):
#         """Called when deleting an attribute: del obj.attr"""
#         if name in self._data:
#             del self._data[name]
#         else:
#             raise AttributeError(f"No such attribute: {name}")

#     def __dir__(self):
#         """Lists available attributes (for autocompletion)"""
#         return list(self._data.keys()) + ['_data']

#     def __repr__(self):
#         return f"DynamicConfig({self._data})"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     print("=== Custom Attribute Access ===")
#     config = DynamicConfig()

#     # __setattr__ demo
#     config.host = "localhost"  # Valid (lowercase)
#     config.port = 8080
#     print(config)  # DynamicConfig({'host': 'VALIDATED_localhost', 'port': 'VALIDATED_8080'})

#     # __getattr__ demo
#     print("Host:", config.host)  # VALIDATED_localhost

#     # __delattr__ demo
#     del config.port
#     print("After deletion:", config)  # DynamicConfig({'host': 'VALIDATED_localhost'})

#     # __dir__ demo
#     print("Available attributes:", dir(config))  # ['host', '_data']

#     # Error cases
#     try:
#         config.Host = "fail"  # Uppercase (__setattr__ blocks)
#     except ValueError as e:
#         print(f"Error: {repr(e)}")  # Attribute names must be lowercase!

#     try:
#         print(config.missing)  # __getattr__ raises
#     except AttributeError as e:
#         print(f"Error: {repr(e)}")  # 'DynamicConfig' has no attribute 'missing'


# class MetaLogger(type):
#     """Metaclass that logs class creation and method calls"""
#     def __new__(cls, name, bases, namespace):
#         print(f"📝 Creating class: {name}")
#         # Add a 'version' attribute to all classes
#         namespace['version'] = "1.0"
#         return super().__new__(cls, name, bases, namespace)

#     def __init_subclass__(cls, **kwargs):
#         """Called when subclass is created"""
#         print(f"🔄 Subclass created: {cls.__name__}")
#         super().__init_subclass__(**kwargs)

# class Document(metaclass=MetaLogger):
#     """Base document class with metaclass logging"""
#     def __class_getitem__(cls, key):
#         """Emulate generic types (e.g., Document[str])"""
#         print(f"🔖 Accessed as generic type: Document[{key}]")
#         return f"Document_{key}"

#     def __mro_entries__(self, bases):
#         """Handle custom MRO entries (advanced inheritance)"""
#         print("🧩 Modifying MRO entries")
#         return bases

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     print("\n=== Class Creation ===")
#     class PDF(Document):  # Triggers MetaLogger.__init_subclass__
#         def __init__(self, name):
#             self.name = name

#     print("\n=== Metaclass in Action ===")
#     print(f"Document version: {Document.version}")  # Added by MetaLogger.__new__
#     print(f"PDF version: {PDF.version}")           # Inherited

#     print("\n=== Class GetItem ===")
#     doc_type = Document[int]  # Triggers __class_getitem__
#     print(f"Type: {doc_type}")

#     print("\n=== MRO Entry (Advanced) ===")
#     class CustomBase: pass
#     entry = Document().__mro_entries__((CustomBase,))
#     print(f"MRO entry: {entry}")

# 1. Define a metaclass (inherits from `type`)
# class Meta(type):
#     def __new__(cls, name, bases, attrs):
#         print(f"🚀 Creating class: {name}")
#         return super().__new__(cls, name, bases, attrs)

# # 2. Use it in a class
# class Cat(metaclass=Meta):
#     pass  # Triggers Meta.__new__

# # Output: "🚀 Creating class: Cat"


# from dataclasses import dataclass, field
# import inspect

# # ===== Metaclass mimicking @dataclass behavior =====
# class DataClassMeta(type):
#     def __new__(cls, name, bases, namespace):
#         """Intercept class creation to add dataclass methods"""
#         print(f"🔧 MetaLogger.__new__: Creating {name}")
#         new_cls = super().__new__(cls, name, bases, namespace)
        
#         # Simulate @dataclass's method generation
#         if '__annotations__' in namespace:
#             for field_name, field_type in namespace['__annotations__'].items():
#                 print(f"  📌 Auto-generating field: {field_name}: {field_type}")
        
#         return new_cls

#     def __init_subclass__(cls, **kwargs):
#         """Hook for subclass creation (used by dataclass inheritance)"""
#         print(f"🔄 MetaLogger.__init_subclass__: {cls.__name__}")
#         super().__init_subclass__(**kwargs)

# # ===== Custom @dataclass with EXPLICIT dunder usage =====
# def dataclass_explained(cls):
#     """DIY @dataclass showing metaprogramming dunders in action"""
#     cls = dataclass(cls)  # Apply standard dataclass first
    
#     # 1. __class_getitem__ for generics (e.g., MyClass[str])
#     original_class_getitem = cls.__class_getitem__ if hasattr(cls, '__class_getitem__') else None
#     def __class_getitem__(cls, item):
#         print(f"✨ __class_getitem__: {cls.__name__}[{item.__name__}]")
#         return original_class_getitem(item) if original_class_getitem else f"{cls.__name__}_{item.__name__}"
#     cls.__class_getitem__ = classmethod(__class_getitem__)
    
#     # 2. __mro_entries__ for inheritance (advanced)
#     def __mro_entries__(self, bases):
#         print(f"🧩 __mro_entries__: Adjusting MRO for {type(self).__name__}")
#         return bases
#     cls.__mro_entries__ = __mro_entries__
    
#     return cls

# # ===== DEMONSTRATION =====
# @dataclass_explained
# class Person(metaclass=DataClassMeta):
#     name: str
#     age: int = field(default=0)
    
#     def __post_init__(self):
#         """Dataclass lifecycle hook"""
#         print(f"🎂 __post_init__: Created {self.name}")

# if __name__ == "__main__":
#     print("\n=== Class Definition ===")
#     # Class creation triggers:
#     # 1. DataClassMeta.__new__
#     # 2. DataClassMeta.__init_subclass__
    
#     print("\n=== Instantiation ===")
#     p = Person("Alice", 30)  # Triggers __post_init__
    
#     print("\n=== Generic Type Access ===")
#     person_type = Person[str]  # Triggers __class_getitem__
#     print(f"Generic type: {person_type}")
    
#     print("\n=== Inheritance (MRO) ===")
#     class Employee(Person):
#         salary: float
#     # Triggers DataClassMeta.__init_subclass__ again


# import copy
# import pickle

# class ShoppingCart:
#     def __init__(self, items=None, discount_code=None):
#         self.items = list(items) if items else []
#         self.discount_code = discount_code
#         # Internal cache (shouldn't be copied)
#         self._cache = {}

#     # Copying
#     def __copy__(self):
#         """Shallow copy (copies only top-level attributes)"""
#         print("🔹 __copy__: Creating shallow copy")
#         new_obj = ShoppingCart()
#         new_obj.items = copy.copy(self.items)
#         new_obj.discount_code = self.discount_code
#         return new_obj

#     def __deepcopy__(self, memo):
#         """Deep copy (recursively copies all objects)"""
#         print(f"🔹 __deepcopy__: Creating deep copy (memo: {memo})")
#         new_obj = ShoppingCart()
#         # Deep copy mutable items
#         new_obj.items = copy.deepcopy(self.items, memo)
#         new_obj.discount_code = copy.deepcopy(self.discount_code, memo)
#         return new_obj

#     # Pickling (serialization)
#     def __reduce__(self):
#         """Controls how the object is pickled"""
#         print("🥒 __reduce__: Preparing for pickling")
#         return (self.__class__, (self.items, self.discount_code))

#     def __reduce_ex__(self, protocol):
#         """Advanced pickling (supports protocol versions)"""
#         print(f"🥒 __reduce_ex__: Using protocol {protocol}")
#         return self.__reduce__()

#     def __repr__(self):
#         return f"ShoppingCart(items={self.items}, discount={self.discount_code})"

# # ===== DEMONSTRATION =====
# if __name__ == "__main__":
#     print("=== Original Cart ===")
#     cart = ShoppingCart(["Apple", "Banana"], "SAVE10")
#     print(cart)

#     print("\n=== Shallow Copy ===")
#     cart_shallow = copy.copy(cart)
#     cart_shallow.items.append("Orange")
#     print("Original:", cart.items)       # ['Apple', 'Banana']
#     print("Shallow Copy:", cart_shallow.items)  # ['Apple', 'Banana', 'Orange']

#     print("\n=== Deep Copy ===")
#     cart_deep = copy.deepcopy(cart)
#     cart_deep.items.append("Milk")
#     print("Original:", cart.items)       # ['Apple', 'Banana']
#     print("Deep Copy:", cart_deep.items)  # ['Apple', 'Banana', 'Milk']

#     print("\n=== Pickling ===")
#     # Pickle (serialize)
#     pickled = pickle.dumps(cart)
#     # Unpickle (deserialize)
#     unpickled = pickle.loads(pickled)
#     print("Unpickled:", unpickled)

# class X :pass
# class Y: pass
# class Z: pass
# class A(X,Y): pass
# class B(Y,Z): pass
# class M(B,A,Z): pass

# print (M.__mro__)

# from functools import partial
# add_five = partial(lambda x, y: x + y, 5)
# print(add_five(3))  # 8

# from functools import reduce

# # Original data
# numbers = [1, 2, 3, 4, 5, 6]

# # Pipeline
# result = reduce(
#     lambda acc, x: acc + x,             # Step 3: Sum the results
#     map(
#         lambda x: x ** 2,               # Step 2: Square each even number
#         filter(
#             lambda x: x % 2 == 0,       # Step 1: Filter even numbers
#             numbers
#         )
#     )
# )

# print(result)  # Output: 56 (2^2 + 4^2 + 6^2 = 4 + 16 + 36)

# class InvalidUserInputError(Exception):
#     """Exception raised when a user provides invalid input."""
    
#     def __init__(self, message, invalid_input=None):
#         super().__init__(message)
#         self.invalid_input = invalid_input

#     def __str__(self): #Dunder for returning strings
#         if self.invalid_input is not None:
#             return f"{self.args[0]} (Invalid input: {self.invalid_input})"
#         return self.args[0]


# def get_user_age():
#     user_input = input("Please enter your age: ")

#     try:
#         age = int(user_input)
#         if age < 0:
#             raise InvalidUserInputError("Age cannot be negative.", invalid_input=user_input)
#         return age
#     except ValueError:
#         raise InvalidUserInputError("The input must be a valid integer.", invalid_input=user_input)
#     except InvalidUserInputError as e:
#         print(f"Error: {e}")
#         return None

# # Example of usage:
# age = get_user_age()
# if age is not None:
#     print(f"Your age is: {age}")
# else:
#     print("Failed to get a valid age.")

# class MultiMessageError(Exception):
#     def __init__(self, msg1, msg2):
#         super().__init__(msg1, msg2)  # passing two values to Exception
# try:
#     raise MultiMessageError("Something went wrong", "Try again later")
# except MultiMessageError as e:
#     print("args:", e.args)
#     print("args[0]:", e.args[0])
#     print("args[1]:", e.args[1])
#     print(e) # output: ('Something went wrong', 'Try again later')



# class InsufficientFundsError(Exception):
#     """Raised when a bank account has insufficient funds."""
    
#     def __init__(self, message, current_balance, withdrawal_amount):
#         super().__init__(message)
#         self.current_balance = current_balance
#         self.withdrawal_amount = withdrawal_amount

#     def __str__(self):
#         return f"{self.args[0]} Current balance: ${self.current_balance}, Requested: ${self.withdrawal_amount}"

# def withdraw_from_account(balance, amount):
#     if amount > balance:
#         raise InsufficientFundsError("Insufficient funds for this withdrawal", balance, amount)
#     return balance - amount

# try:
#     balance = 100
#     withdrawal = 150
#     new_balance = withdraw_from_account(balance, withdrawal)
# except InsufficientFundsError as e:
#     print(f"Error: {e}")


# import logging
# from logging.handlers import RotatingFileHandler
# import sentry_sdk  # External error tracking

# # Initialize Sentry (only captures ERROR+)
# sentry_sdk.init("YOUR_SENTRY_DSN")

# # Create logger
# logger = logging.getLogger("my_app")
# logger.setLevel(logging.DEBUG)  # Lowest level (capture everything)



# # --- Handlers (where logs go) ---
# # 1. Console (INFO+ only)
# console_handler = logging.StreamHandler()
# console_handler.setLevel(logging.INFO)  # Ignore DEBUG logs here

# # 2. Rotating File (WARNING+)
# file_handler = RotatingFileHandler(
#     "app.log", maxBytes=1e6, backupCount=3  # 1MB per file, keep 3 backups
# )
# file_handler.setLevel(logging.WARNING)

# # 3. Error-only File (ERROR+)
# error_handler = logging.FileHandler("errors.log")
# error_handler.setLevel(logging.ERROR)



# # --- Formatters (how logs look) ---
# formatter = logging.Formatter(
#     "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
# )
# console_handler.setFormatter(formatter)
# file_handler.setFormatter(formatter)
# error_handler.setFormatter(formatter)


# # Attach handlers
# logger.addHandler(console_handler)
# logger.addHandler(file_handler)
# logger.addHandler(error_handler)


# # --- Example Usage ---
# logger.debug("Debug detail (only visible if level=DEBUG)")      # Goes nowhere in prod (unless you change levels)
# logger.info("System started")                                  # Console only
# logger.warning("Low disk space")                               # Console + app.log
# logger.error("Payment failed", extra={"user_id": 123})         # Console + app.log + errors.log + Sentry

# import pdb

# def divide(a, b):
#     result = a / b  # Potential ZeroDivisionError
#     return result

# pdb.set_trace()
# print(divide(10, 0))

# from collections import Counter,defaultdict,OrderedDict

#Counter counts the number of occurence

# name = "Alfredo Torrena"
# count= Counter(name)
# print (type(count)) # <class 'collections.Counter'>
# print(count)

# dictionary = defaultdict(lambda: "Not present", {'a': 1, 'b': 2})
# print(dictionary)
# print(dictionary['a'])
# print(dictionary['c'])

# from collections import OrderedDict

# print("dict")
# #d = OrderedDict()
# d ={}
# d['a'] = 1
# d['b'] = 2
# d['c'] = 3
# d['d'] = 4
# print(d)
# for key, value in d.items():
#     print(key, value, end= " , ")

# print( "\nordered dict")
# od = OrderedDict()
# od['d'] = 4
# od['b'] = 2
# od['a'] = 1
# od['c'] = 3
# print(od)
# for key, value in od.items():
#     print(key, value, end= " , ")

# print(d == od) # output = false

import sys 
# for line in sys.stdin: 
# 	if 'q' == line.rstrip(): 
# 		break
# 	print(f'Input : {line}') 

# print("Exit") 
print(sys.version_info)
print(sys.platform)
print(sys.path)

