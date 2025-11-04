import math
import pytest
from app.operations import add, subtract, multiply, divide, power, modulo

def test_add():
    assert add(2, 3) == 5.0
    assert add(-1, 1) == 0.0

def test_subtract():
    assert subtract(5, 3) == 2.0
    assert subtract(0, 2) == -2.0

def test_multiply():
    assert multiply(4, 2.5) == 10.0
    assert multiply(-3, 3) == -9.0

def test_divide_basic():
    assert divide(10, 2) == 5.0
    assert math.isclose(divide(1, 3), 0.3333333333333, rel_tol=1e-9)

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

def test_power():
    assert power(2, 3) == 8.0

def test_modulo():
    assert modulo(10, 3) == 1.0

def test_modulo_by_zero():
    with pytest.raises(ZeroDivisionError):
        modulo(1, 0)
