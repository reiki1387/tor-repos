import pytest
from calculator import factorial,is_prime,power


def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1          #factorial of 1 is always zero
    with pytest.raises(ValueError):   #1 and negatve numbers cannot be factorial
        factorial(4)

def test_is_prime():
    assert is_prime(2) is True
    assert is_prime(4) is False
    assert is_prime(13) is True
    assert is_prime(1) is False

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1
    assert power(7, 2) == 49