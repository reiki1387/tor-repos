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
#         return "Function from Parent1"

# class Parent2:
#     def function2(self):
#         return "Function from Parent2"

# class Child(Parent1, Parent2):
#     pass  # Inherits all methods from Parent1 and Parent2

# child = Child()
# print(child.function1())  # ✅ Output: Function from Parent1
# print(child.function2())  # ✅ Output: Function from Parent2

# print(Child.__mro__) #(<class '__main__.Child'>, <class '__main__.Parent1'>, 
#                      #<class '__main__.Parent2'>, <class 'object'>)



class A:
    def speak(self):
        print("speak method from A")
        return "Method from A"

class B:
    def speak(self):
        print("speak method frm B")
        return "Method from B"

class C(A, B):
    def speak(self):
        print("speak method from C")
        return super().speak() + " and  Method from class C is also called" # Call the next class's speak() in MRO

c = C()
print(c.speak())  # This will use super() to call the method from class A.

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






