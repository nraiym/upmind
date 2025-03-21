# Если на улице дождь
#     Взять зонт
# Иначе
#     Выйти без зонта
# Условные конструкторы (if elif else)

# is_rainy = True
# if is_rainy:
#     print("Is rainy")
# else:
#     print("Is not rainy")

# login = input("Enter your login:")
# password = input("Enter your password:")
# if login == "admin" and password == "1234":
#     print("Login successful")
# else:
#     print("Login failed")


# is_cold = True
#
# if is_cold:
#     print("Take a hot tea:")
#
#     is_cold = False
#     print("You are in if")
#
# print("You are not in if")


#2. Синтаксис условных операторов в Python
# Оператор if

# if age >= 18:
#     print("Вы совершеннолетний")

# Условие должно возвращать True или False.
# Код после if выполняется только если условие истинно.
#
# Оператор if-else
# age = 16
# if age >= 18:
#     print("Вы совершеннолетний")
# else:
#     print("Вы несовершеннолетний")
#Блок else выполняется, если усовие if ложно

#Оператор if-elif-else
# score = 85
# if score >= 90:
#     print("Отлично")
# elif score >= 70:
#     print ("Хорошо")
# else:
#     print("Нужно постараться:")
#elif добавляет дополнительные условия
# Код проверяет условия сверху вниз
# Правильное форматирование (отступы)
# Важно использовать одинаковые отступы (4 пробела)


#Вложенные условия
# age = 20
# has_license = True
#
# if age >= 18:
#     if has_license:
#         print("Вы можете водить машину")
#     else:
#         print("Получите водительские права")
# else:
#     print("Вы слишком молоды для вождения")

#Вложенные условия помогают уточнить проверки
#Лучше избегать глубокой вложенности

#Логические операторы в условиях

#5. Логические операторы в условиях
#Объяснение операторов and, or, not:

# age = 25
# income = 40000
#
# if not age <= 18 and income > 30000:
#     print("Вы можете взять кредит")

# and - Оба условия должны быть истинными
# or - хотя бы одно условие должно быть истинным
# not - конвертирует значение условия

#6. Тернарный оператор (10 минут)
# Объяснение краткой записи условий

age = 20
message = "Совершеннолетний" if age >= 18 else "Несовершеннолетний"
print (message)