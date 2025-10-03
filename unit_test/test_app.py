import unittest
from app import calculate_area, is_palindrome 

class TestGeometry(unittest.TestCase):
    def test_area_normal_case(self):
        self.assertEqual(calculate_area(5, 10), 50)

    def test_area_with_zero(self):
        self.assertEqual(calculate_area(8, 0), 0)

    def test_area_raises_error_on_negative(self):
        with self.assertRaises(ValueError):
            calculate_area(-5, 10)

if __name__ == '__main__': # если файл не модуль
    unittest.main() # запуск тестов

