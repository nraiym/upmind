# # решетки для каких-то заметок, комментариев
# """
# многострочные комментарии
# много строк между 3 кавычками
# """
#
# # int - (числа/integer) неизменяемый целочисленный тип данных
# num1 = 1
# num2 = 2
# num3 = 3
# from operator import truediv

# str - (строка/tring) неименяемый строковой тип данных
# s1="string"
# s2='string'



# print(num1)
# user_number = input("enter a number: ")
# print("User entered: ", user_number)
#
# # все что слева от равно - название, все что справа - содержимое
#
# # print() - вывод в консоль, принимает на вход переменные, можно через запятую
# # input() - ввод с консоли, принимает на вход текст который выведет в консоль для ввода
# # type() - выводит тип данных переменной, принимает на вход переменную
# # len() - выводит длину объекта, принимает на вход переменную
# # int() - приведение к типу integer
# # str() - приведение к типу string
# #float() - приведение к типу float
# # Lower() - метод строки переводящий всю строку в нижний регистр



# print(num1)
# enter = input("Enter number: ")
# print("User entered: ", int(user_number))
#
# age = int(input("Введите ваш возраст: ")) #ввод числа
# print("Ваш возраст:", age)
# print(type(age)) # <class 'int'>

# a = 10
# b = 3
# print(a + b) # 13 (сложение)
# print(a - b) # 7 (вычитание)
# print(a * b) # 30 (умножение)
# print(a // b) # 3 (целочисленное деление)
# print(a % b) # 1 (остаток от деления)
# print(a ** b) #1000 (возведение в степень)


# name = input("Введите ваше имя: ") # Ввод строки
# print("Привет, " + name + "!")
# print(type(name)) # ‹class 'str'>
# text = """ Это многострочный текст
# в Python"""
# print(text)
# word = "Python"
# print (word[0]) # P
# print(word[-1]) # n
# print (len(word)) # 6
# number = 42
# num_str = str (number)
# print(type(num_str)) # <class 'str'>

# pi = float(input("Введите число с плавающей точкой: ")) # Ввод float
# print("Вы ввели:", pi)
# print(type(pi)) # <class ' float'>
# print(round (pi, 2)) # Округление
#
# num_str = "3.5"
# num_float = float(num_str)
# print(type(num_float)) #‹class 'float'>
#
# # str - (строка/tring) изменяемый ятроковый тигданных
# s1 = "string"
# enter = 'Логин'


# a = 10
# b = 3
# # bool - может иметь только два состояния: True or False
# is_python_easy = input("Python легкий? (да/нет): "). lower() == "да" # Ввод bool
# print("Вы ответили:", is_python_easy)
# print(type (is_python_easy)) # <class 'bool'>
# print(a > b) # False
# print(a < b) # True
# print(a == b) # False
# print(a != b) # True
# print(True and False) # False
# print(True or False) # True
# print(not True) # False


# #Преобразование типов
# print(float(5)) # 5.0
# print(int(5.9)) #5
# print (int("100")) # 100
# print(str(42)) # "42"
# print(int(True)) # 1 #всегда тру 1 фолс 0
# print (int(False)) # 0

#task1
# #x = 18
# age = int(input("Сколько вам лет?"))
# print("Ваш возраст:")
# print(age >= 18)

# age = int(input("Введите ваш возраст: "))
# print(True if age >= 18 else False)

#task2
# x = int(input("Введите целое число"))
# y = float(input("Введите дробное число"))
# print(x + y)
# print(x - y)
# print(x / y)
# print(x * y)
# print(x // y)
# print(x ** y)
# print(x % y)

#task3
# #login = type(input("Введие логин:")
# #password = type(input("Введите пароль:")
# #print("Доступ разрешен" if login == "admin" and password == "1234")
# #else
# #print("Доступ запрещен")

#correct
# login = input("Введие логин:")
# password = input("Введите пароль:")
# if login == "admin" and password == "1234":
#     print("Доступ разрешен")
# else:
#     print("Доступ запрещен")


# login = input("Введите логин:")
# password = input("Введите пароль")
# print(login == "admin" and password == "1234")

#task4
# number = int(input("Напишите целое число"))
# # 1
# if number % 2 == 0:
#     print(True)
# else:
#     print(False)

# #2
# print(True if number % 2 == 0 else False)

#3 #correcteasy
# print(number % 2 == 0)

#task5
# x = int(input("Введите первое число:"))
# y = int(input("Введите второе число:"))
# z = int(input("Введите третье число:"))
# print(round((x + y + z)/3, 2))

#task6
# num = int(input("Введите четырехзначное число:"))
# if 1000 <= num <= 9999:
#     print(f"Вы ввели число:{num}")
#     a, b, c, d = map(int, str(num))
#     numsum = a + b + c + d
#     print(f"Сумма всех цифр: {numsum}")
#     if str(num) == str(num)[::-1]:
#         print("Это число - палиндром:")
#     else:
#         print("Это число - НЕ палиндром:")
# else:
#     print("Ошибка, введите четырехзначное число:")
#
# #correct
# num = input("Введите четырехзначное число:")
# print(1000 <= int(num) <= 9999)
# print(int(num[0]) + int(num[1]) + int(num[2]) + int(num[3]))
# print(int(num[0]) == int(num[3]) and int(num[1]) == int(num[2]))


# num = -10
# print("Absolute value", abs(num))
# print("Max of(10, 20, 30):", max(10, 20, 30))
# print("Min of(10, 20, 30):", min (10, 20, 30))
# print("Power (2^3) using pow():", pow(2, 3))
# print("Power (2^3) using **:", 2 ** 3)
# print("Convert '100' to int:", int("100"))
# print("Convert float 3.9 to int:", int(3.9))  # Rounds down
#
# fnum = -7.8
# print("Absolute value:", abs(fnum))
# print("Round 4.678:", round(4.678))
# print("Round 4.678 to 2 decimals:", round(4.678, 2))
# print("Convert '10.5' to float:", float("10.5"))


#hw2
# num = int("250")
# print(num)
# num2 = float(14.75)
# print(int(num2))
# print(int(num) + int(num2))

# Поиск максимального и минимального значения
# print("\n2️⃣ Поиск максимального и минимального значения")
# - Даны числа: 45, 12, 89, 32, 67.
# - Найдите:
#   - Максимальное значение.
#   - Минимальное значение.


# print("Max of (45, 12, 89, 32, 67)", max(45, 12, 89, 32, 67))
# print("Min of (45, 12, 89, 32, 67)", min(45, 12, 89, 32, 67))

# ️⃣ Возведение в степень
# print("\n3️⃣ Возведение в степень")
# - Вычислите 3 в степени 4 с помощью pow().
# - Сделайте то же самое с помощью **.

# print("3 in power of 4 =", pow(3,4))
# print("3 in power of 4 =", 3**4)

# ️⃣ Абсолютное значение и округление
# print("\n4️⃣ Абсолютное значение и округление")
# - Найдите абсолютное значение числа -100.
# - Округлите 5.786 до 2 десятичных знаков.

# num = int(-100)
# print("Absolute value:", abs(num))
# print(round(5.786,2))

# Преобразование строки в число с плавающей точкой
# print("\n5️⃣ Преобразование строки в float")
# # - Преобразуйте строку "45.99" в float.
# # - Преобразуйте 18 (целое число) в float.
# # - Сложите оба числа и выведите результат.

# num = str("45.99")
# print(float(num))
#
# num18 = int("18")
# print(float(num18))
# print(float(num) + float(num18))

# ️⃣ Округление чисел
# print("\n6️⃣ Округление чисел")
# - Округлите 9.8765 до 3 десятичных знаков.
# - Округлите 7.4 до ближайшего целого числа.

# print(round(float(9.8765), 3))
# print(int(7.4))

# 7️⃣ Изменение регистра строки
# print("\n7️⃣ Изменение регистра строки")
# - Преобразуйте строку "python programming" в:
#   - ВЕРХНИЙ РЕГИСТР.
#   - нижний регистр.
#   - Заглавные слова (Title case).

# text = str("python programming")
# print("Uppercase:", text.upper())
# print("Lowercase:", text.lower())
# print("Title Case:", text.title())


# ️⃣ Удаление лишних пробелов
# print("\n8️⃣ Удаление лишних пробелов")
# - Дана строка "   Code in Python   ":
#   - Удалите пробелы слева.
#   - Удалите пробелы справа.
#   - Удалите пробелы с обеих сторон.

# text = str("   Code in Python   ")
# print("Stripped spaces:", text.strip())
# print("Left stripped:", text.lstrip())
# print("Right stripped:", text.rstrip())

# 9️⃣ Поиск и замена в строке
# print("\n9️⃣ Поиск и замена в строке")
# - Дана строка "Learning Python is fun":
#   - Найдите индекс слова "Python".
#   - Замените "fun" на "awesome".

# text = str("Learning Python is fun")
# print("Index of 'Python':", text.find("Python"))
# print("Replace 'fun' with 'awesome':", text.replace("fun","awesome"))


# 🔟 Разделение и объединение строк
# print("\n🔟 Разделение и объединение строк")
# - Преобразуйте строку "apple,banana,grape" в список.
# - Объедините список обратно в строку, разделяя элементы с помощью " | ".

fruits = "apple, banana, grape"
words = fruits.split(",")
print(words)
print("|".join(words))


# # 1️⃣1️⃣ Проверка содержимого строки
# print("\n1️⃣1️⃣ Проверка содержимого строки")
# - Проверьте, состоит ли "54321" только из цифр.
# - Проверьте, является ли "" буквенно-цифровым значением.
# - Проверьте, состоит ли "PYTHON" только из заглавных букв.

# print("Is '54321' all digits?:", "54321".isdigit())
# print("Is 'Hello123' alphanumeric?:", "Hello123".isalnum())
# print("Is 'PYTHON' uppercase?:", "PYTHON".isupper())

# 1️⃣2️⃣ Форматирование строк с помощью f-строк
# print("\n1️⃣2️⃣ Форматирование строк с f-strings")
# - Сохраните "David" в переменную name.
# - Сохраните 30 в переменную age.
# - Выведите строку "Меня зовут David, и мне 30 лет." с помощью f-строк.

# name = str("David")
# age = str("30")
# print(f"Меня зовут {name} и мне {age} лет.")

# # 1️⃣3️⃣ Преобразование значений в булево
# print("\n1️⃣3️⃣ Преобразование значений в bool")
# - Определите булево значение для:
#   - 0
#   - 1
#   - "" (пустая строка)
#   - "Hello"
#   - None
#   - [] (пустой список)
#   - [1, 2, 3] (непустой список)

# print("Boolean of 0:", bool(0))
# print("Boolean of 1:", bool(1))
# print("Boolean of "":", bool(""))
# print("Boolean of Hello:", bool("Hello"))
# print("Boolean of None:", bool(None))
# print("Boolean of []", bool([]))
# print("Boolean of [1, 2, 3]:", bool([1, 2, 3]))

# # 1️⃣4️⃣ Булева логика
# print("\n1️⃣4️⃣ Булева логика")
# - Даны:
#   x = True
#   y = False
#   - Найдите результат выражений:
#     - x and y
#     - x or y
#     - not x

# x = True
# y = False
# print(x and y)
# print(x or y)
# print(not x)


# 🎯 Дополнительное задание: ввод данных и проверка возраста
# print("\n🎯 Дополнительное задание: ввод данных и проверка возраста")

# - Попросите пользователя ввести его имя.
# - Попросите ввести возраст (в виде строки, затем преобразуйте в целое число).
# - Проверьте, исполнилось ли пользователю 18 лет, и выведите:
#   - "Вы совершеннолетний", если возраст >= 18.
#   - "Вы несовершеннолетний" в противном случае.
# - Отформатируйте вывод с помощью f-строки.

# name = input("Введите имя:")
# print(name)
# age = input(str("Введите возраст:"))
# print(int(age))
# age2 = int(age)
# print(age2 >= 18)
# if age2 >= 18:
#     print("Вы совершеннолетний")
# else:
#     print("Вы несовершеннолетний")
# print(f"Ваше имя {name} и вам {age} лет")



