import pytest
from calculator import Calculator

def test_add_positive_numbers():
    calc = Calculator()
    assert calc.add(2, 3) == 5

def test_add_negative_numbers():
    calc = Calculator()
    assert calc.add(-2, -3) == -5

def test_subtract_positive_numbers():
    calc = Calculator()
    assert calc.subtract(10, 4) == 6

def test_subtract_result_negative():
    calc = Calculator()
    assert calc.subtract(3, 10) == -7

def test_multiply_positive_numbers():
    calc = Calculator()
    assert calc.multiply(6, 7) == 42

def test_multiply_by_zero():
    calc = Calculator()
    assert calc.multiply(999, 0) == 0

def test_divide_normal_case():
    calc = Calculator()
    assert calc.divide(8, 2) == 4

def test_divide_by_zero_raises():
    calc = Calculator()
    with pytest.raises(ValueError):
        calc.divide(5, 0)
