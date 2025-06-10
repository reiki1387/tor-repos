def multiply(func):
    #wrapper is nested function. This function will replace the original function (in this case, add).
    def wrapper(a, b):
        #func(a, b)  will call add(a, b) and stores its result in the variable result
        result = func(a, b)
        return result * 2  # Multiplies the result by 2
    return wrapper

#The @multiply syntax is a decorator that wraps the add function with multiply
#Now, whenever add is called, it first executes the wrapper function inside multiply.
@multiply
def add(a, b):
    return a + b

# Example usage
result = add(3, 4)  # (3 + 4) * 2
print(result)  # Output: 14



#Without using auto decorator
def multiply(func):
    def wrapper(a, b):
        result = func(a, b)
        return result * 2  # Multiplies the result by 2
    return wrapper

def add(a, b):
    return a + b

# Manually applying the decorator
add = multiply(add)

# Example usage
result = add(3, 4)  # (3 + 4) * 2
print(result)  # Output: 14



# defining a body of a function inside another function without decorator
#can be poblematic in some cases
def multiply(func, a, b):
    result = func(a, b)  # Call the passed function
    return result * 2  # Multiply the result by 2

def add(a, b):
    return a + b  # The body of this function can be passed

# Passing the body of 'add' to 'multiply'
result = multiply(add, 3, 4)  # (3 + 4) * 2
print(result)  # Output: 14
