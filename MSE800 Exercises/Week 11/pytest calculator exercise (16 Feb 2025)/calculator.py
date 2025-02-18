import math
import pytest

def factorial(n):
    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers")
    return math.factorial(n)

def is_prime(n):
    if n < 2:    #checks that number is not 1
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def power(base, exp):
    return base ** exp



#calcuates factorial and checks for prime number , if input is one input
#calculates the power if user input two input
def calculator(): #split() automatically converts input to lists
    user_input = input("Enter one or two numbers separated by space: ").strip().split() 
    
    # additional condition to check for negative number        " or (num[1:].isdigit() and num[0] == '-') "
    try: 
        numbers = [int(num) for num in user_input if num.isdigit() ]
    except ValueError:
        print("Invalid input! Please enter numeric values only.")
        return

    #checks if the new list contains the original lists of user input
    if len(numbers) != len(user_input):
        print("Invalid input! Please enter numeric values only.")
        return

    if len(numbers) == 1:
        num = numbers[0]
        print(f"Factorial of {num}: {factorial(num)}")
        print(f"Is {num} a prime number? {'Yes' if is_prime(num) else 'No'}")
    elif len(numbers) == 2:
        base, exp = numbers  #tuples unpacking
        print(f"{base} raised to the power of {exp}: {power(base, exp)}")   
    else:
        print("Invalid input! Please enter one or two numbers.")

if __name__ == "__main__":
    calculator()

# Unit tests using pytest in separate file

