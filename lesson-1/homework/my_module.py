import threading
import time
import logging

# Настройка логирования для наглядности
logging.basicConfig(level=logging.INFO, format='%(threadName)s: %(message)s')

def task_a(name):
    """Метод, выполняемый первым потоком."""
    logging.info(f"Поток '{name}' запущен.")
    for i in range(1, 6):
        logging.info(f"Шаг {i}")
        time.sleep(0.1)  # Имитация работы
    logging.info(f"Поток '{name}' завершен.")

def task_b(count):
    """Метод, выполняемый вторым потоком с параметром."""
    logging.info(f"Поток запущен. Макс. итераций: {count}")
    for i in range(1, count + 1):
        logging.info(f"\tИтерация {i}")
        time.sleep(0.2)  # Имитация работы
    logging.info("Поток завершен.")

if __name__ == "__main__":
    logging.info("Основной поток начал работу.")

    # 1. Создание потока для TaskA
    thread_a = threading.Thread(target=task_a, args=("Task_A_Worker",), name="Thread-A")

    # 2. Создание потока для TaskB с передачей параметра
    thread_b = threading.Thread(target=task_b, args=(3,), name="Thread-B")

    # 3. Запуск потоков
    thread_a.start()
    thread_b.start()

    # 4. Ожидание завершения потоков с помощью join()
    thread_a.join()
    thread_b.join()

    logging.info("Основной поток завершен. Все потоки отработали.")