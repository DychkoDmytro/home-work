# Числовые типы данных
x = 10      # целое число (int)
y = 3.14    # число с плавающей точкой (float)

# Строки
name = "John"  # строка (str)

# Логический тип данных
is_active = True  # булевый тип (bool)

# Списки (массивы)
numbers = [1, 2, 3, 4, 5]

# Кортежи (неизменяемые списки)
coordinates = (50.45, 30.52)

# Словари (key-value пары)
person = {"name": "John", "age": 30}




a = 5
b = 2

# Сложение
sum = a + b  # 7

# Вычитание
difference = a - b  # 3

# Умножение
product = a * b  # 10

# Деление
quotient = a / b  # 2.5

# Целочисленное деление
floor_division = a // b  # 2

# Остаток от деления
modulus = a % b  # 1

# Возведение в степень
power = a ** b  # 25



s = "Hello, World!"

# Доступ к символам
first_char = s[0]  # 'H'

# Длина строки
length = len(s)  # 13

# Изменение регистра
lower_case = s.lower()  # 'hello, world!'
upper_case = s.upper()  # 'HELLO, WORLD!'

# Конкатенация (объединение строк)
greeting = "Hello" + " " + "John"  # 'Hello John'

# Форматирование строк
name = "John"
age = 30
message = f"My name is {name}, and I am {age} years old."
# 'My name is John, and I am 30 years old.'



x = 10
y = 20

if x > y:
    print("x больше, чем y")
elif x < y:
    print("x меньше, чем y")
else:
    print("x и y равны")


    #пример
name = "Dmytro"
age = 34

if age < 18:
    print("Ты еще слишком молод.")
elif age <= 18 > 30:
    print("Ты в самом расцвете сил")    
else :
    print("Ты уже мудрый")      



    # Перебор элементов списка
numbers = [1, 2, 3, 4, 5]
for number in numbers:
    print(number)

# Перебор символов в строке
word = "Python"
for char in word:
    print(char)

    # Пример с while
count = 0
while count < 5:
    print("Счетчик:", count)
    count += 1  # Увеличиваем значение на 1

    # Прерывание цикла
for i in range(10):
    if i == 5:
        break  # Выходим из цикла, когда i равно 5
    print(i)



# Пропуск итерации
for i in range(10):
    if i % 2 == 0:
        continue  # Пропускаем итерации для четных чисел
    print(i)

    # Пример функции
def greet(name):
    print(f"Привет, {name}!")

greet("Dmytro")  # Выведет: Привет, Dmytro!

# Пример функции с возвращаемым значением
def add(a, b):
    return a + b

result = add(5, 3)
print(result)  # 8

def greet(name="гость"):
    print(f"Привет, {name}!")

greet()           # Выведет: Привет, гость!
greet("Dmytro")   # Выведет: Привет, Dmytro!


# пример
def life_stage(age):
    if age < 18:
        print("Ты еще слишком молод.")
    elif 18 <= age <= 30:
        print("Ты в самом расцвете сил!")
    else:
        print("Ты уже мудрый.")

# Вызов функции с возрастом 34
life_stage(34)  # Выведет: Ты уже мудрый.

greet("Dmytro")  # Привет, Dmytro!


def calculate_max(*numbers):
    if len(numbers) ==0:
        return "Максимальное."
    return max(numbers) 

print(calculate_max(1, 74, 33, 3, 83,99))

def introduce(name, age):
    return f"Меня зовут {name}, и мне {age} лет."

print(introduce("Дмитрий", 34))