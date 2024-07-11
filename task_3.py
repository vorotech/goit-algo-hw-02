#
# Завдання 3
#
# У багатьох мовах програмування ми маємо справу з виразами, виділеними
# символами-розділювачами, такими як круглі ( ), квадратні [ ] або фігурні дужки { }.
#
# Напишіть програму, яка читає рядок з послідовністю символів-розділювачів,
# наприклад, ( ) { [ ] ( ) ( ) { } } }, і надає відповідне повідомлення, коли розділювачі
# симетричні, несиметричні, наприклад ( ( ( ) , або коли розділювачі різних видів стоять
# у парі, як-от ( }.
#
# 💡 Використовуйте стек, щоб запам'ятати відкриті в даний момент символи-розділювачі.
#
# Приклад очікуваного результату:
#
# ( ){[ 1 ]( 1 + 3 )( ){ }}: Симетрично
# ( 23 ( 2 - 3);: Несиметрично
# ( 11 }: Несиметрично

class Stack:
    def __init__(self):
        self.stack = []

    # Додавання елемента до стеку
    def push(self, item):
        self.stack.append(item)

    # Видалення елемента зі стеку
    def pop(self):
        if len(self.stack) < 1:
            return None
        return self.stack.pop()

    # Перевірка, чи стек порожній
    def is_empty(self):
        return len(self.stack) == 0

    # Перегляд верхнього елемента стеку без його видалення
    def peek(self):
        if not self.is_empty():
            return self.stack[-1]

def log_input(func):
    def wrapper(input_string):
        print(input_string)
        return func(input_string)
    return wrapper

@log_input
def is_balanced(input_string):
    # Словник для перевірки відповідності дужок
    brackets = {'(': ')', '[': ']', '{': '}'}
    open_brackets = brackets.keys()
    close_brackets = brackets.values()

    # Стек для збереження відкритих дужок
    stack = Stack()

    # Перебір символів у рядку
    for char in input_string:
        if char in open_brackets:
            stack.push(char)
        elif char in close_brackets:
            if stack.is_empty():
                return "Несиметрично"
            last_open = stack.pop()
            if brackets[last_open] != char:
                return "Несиметрично"

    # Перевірка, чи залишилися незакриті дужки
    if not stack.is_empty():
        return "Несиметрично"

    return "Симетрично"

# Перевірка
print(is_balanced("( ){[ 1 ]( 1 + 3 )( ){ }}"))  # Симетрично
print(is_balanced("( 23 ( 2 - 3);"))             # Несиметрично
print(is_balanced("( 11 }"))                     # Несиметрично
print(is_balanced("( {)[ 1 ]}"))                 # Несиметрично
