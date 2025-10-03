import unittest # импорт библиотеки для юнит-тестирования

def get_sum(num1, num2): # тестируемая функция
    return num1 + num2 # возвращает сумму двух чисел

class TestSum(unittest.TestCase): # создание класса, который будет содержать методы для тестирования
    def test_get_sum(self): # метод тестирующий функцию get_sum()
        self.assertEqual(get_sum(2, 3), 4) # с помощью встроенного метода assertEqual() проверка возвращаемого значения

if __name__ == '__main__': # если файл не модуль
    unittest.main() # запуск тестов
   
