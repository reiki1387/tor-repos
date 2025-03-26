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

def log_decorator(func):
    def wrapper(*args, **kwargs):  # Wrapper function takes any arguments
        print(f"Calling {func.__name__} with {args} {kwargs}")  # Logs function name and arguments
        return func(*args, **kwargs)  # Calls the original function
    return wrapper  # Returns the wrapper function (not calling it yet!)

@log_decorator
def say_hello(name):
    print(f"Hello, {name}")

#This is manual calling by decorator
# def say_hello(name):
#     print(f"Hello, {name}")

# say_hello = log_decorator(say_hello)  # Decorate the function

say_hello("Alice")
