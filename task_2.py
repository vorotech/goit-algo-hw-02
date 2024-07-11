#
# Завдання 2
#
# Необхідно розробити функцію, яка приймає рядок як вхідний параметр, додає всі його символи до
# двосторонньої черги (deque з модуля collections в Python), а потім порівнює символи з обох кінців
# черги, щоб визначити, чи є рядок паліндромом. Програма повинна правильно враховувати як рядки
# з парною, так і з непарною кількістю символів, а також бути нечутливою до регістру та пробілів.
#

from collections import deque

def log_input(func):
    def wrapper(input_string):
        print(input_string)
        return func(input_string)
    return wrapper

@log_input
def is_palindrome(input_string):
    '''Функція перевіряє чи є рядок паліндромом'''

    # Привести рядок до нижнього регістру і видалити пробіли
    normalized_string = ''.join(char.lower() for char in input_string if char.isalnum())

    # Додати всі символи до двосторонньої черги
    char_deque = deque(normalized_string)

    # Порівняти символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False
    return True

# Перевірка
print(is_palindrome("Racecar"))                      # True
print(is_palindrome("А роза упала на лапу Азора"))   # True
print(is_palindrome("Я несу гусеня"))                # True
print(is_palindrome("Hello, World!"))                # False
