
# Файл: test_my_module.py
import pytest
from my_module import add

def test_positive_numbers():
    # Тест 1
    assert add(5, 3) == 8

def test_negative_numbers():
    # Тест 2
    assert add(-10, 5) == -5

def test_float_numbers():
    # Тест 3
    assert add(1.5, 2.5) == 4.0

def test_zero_numbers():
    # Тест 4
    assert add(0, 0) == 0
