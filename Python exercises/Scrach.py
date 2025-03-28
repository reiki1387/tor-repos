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


def super_func(*args, **kwargs):
    print( type(args))
    print( type(kwargs))
    return sum(args)

print(super_func(1,2,3,4,5, x=5,y=6,z=7))