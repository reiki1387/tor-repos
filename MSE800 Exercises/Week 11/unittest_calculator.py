import math
import unittest

# Base class
class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

# First Child Class (Basic Operations)
class BasicCalculator(Calculator):
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

# Second Child Class (Advanced Operations)
class AdvancedCalculator(Calculator):
    def factorial(self, n):
        if n < 0:
            raise ValueError("Factorial is not defined for negative numbers")
        return math.factorial(n)
    
    def power(self, base, exp):
        return base ** exp

# Unit testing using unittest
class TestCalculator(unittest.TestCase):
    
    def setUp(self):
        self.basic_calc = BasicCalculator()
        self.adv_calc = AdvancedCalculator()
    
    def test_addition(self):
        self.assertEqual(self.basic_calc.add(3, 5), 8)
        self.assertEqual(self.adv_calc.add(-2, 2), 0)
    
    def test_factorial(self):
        self.assertEqual(self.adv_calc.factorial(5), 120)
        with self.assertRaises(ValueError):
            self.adv_calc.factorial(-1)

if __name__ == "__main__":
    unittest.main()