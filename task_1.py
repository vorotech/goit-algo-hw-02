#
# Завдання 1
#
# Потрібно розробити програму, яка імітує приймання й обробку заявок: програма має автоматично
# генерувати нові заявки (ідентифіковані унікальним номером або іншими даними), додавати їх
# до черги, а потім послідовно видаляти з черги для "обробки", імітуючи таким чином роботу
# сервісного центру.
#
# Ось псевдокод для завдання з використанням черги (Queue з модуля queue в Python) для
# системи обробки заявок:
#
# import Queue
#
# Створити чергу заявок
# queue = Queue()
#
# Функція generate_request():
#     Створити нову заявку
#     Додати заявку до черги
#
# Функція process_request():
#     Якщо черга не пуста:
#         Видалити заявку з черги
#         Обробити заявку
#     Інакше:
#         Вивести повідомлення, що черга пуста
#
# Головний цикл програми:
#     Поки користувач не вийде з програми:
#         Виконати generate_request() для створення нових заявок
#         Виконати process_request() для обробки заявок
#
# У цьому псевдокоді використовуються дві основні функції: generate_request(), яка генерує
# нові заявки та додає їх до черги, та process_request(), яка обробляє заявки, видаляючи їх
# із черги. Головний цикл програми виконує ці функції, імітуючи постійний потік нових заявок
# та їх обробку.
#

import queue
import threading
import time
import random

# Створити чергу заявок
request_queue = queue.Queue()

# Флаг завершення
exit_flag = False

def generate_request():
    '''Функція для генерації нових заявок'''

    # Унікальний ідентифікатор для заявок
    request_id = 0

    while not exit_flag:
        request_id += 1
        new_request = f"Запит {request_id}"
        request_queue.put(new_request)
        print(f"Згенеровано: {new_request}")
        # Затримка для імітації часу між заявками
        time.sleep(random.randint(1, 5))

def process_request():
    '''Функція для обробки заявок'''

    while not exit_flag:
        if not request_queue.empty():
            request = request_queue.get()
            print(f"В обробці: {request}")
            # Імітація часу обробки заявки
            time.sleep(random.randint(1, 4))
            print(f"Оброблено: {request}")
        else:
            print("Черга порожня, чекаємо нових запитів...")
            time.sleep(1)

# Головний цикл програми
if __name__ == "__main__":
    print("Запуск програми. Для виходу натисніть Ctrl+C")

    # Створити потоки для генерації та обробки заявок
    generate_thread = threading.Thread(target=generate_request)
    process_thread = threading.Thread(target=process_request)

    # Запуск потоків
    generate_thread.start()
    process_thread.start()

    try:
        while True:
            time.sleep(0.1)
    except KeyboardInterrupt:
        print("Отриманий сигнал виходу, вимкнення...")
        exit_flag = True
        # Приєднання потоків до головного потоку
        generate_thread.join()
        process_thread.join()
