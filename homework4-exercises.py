# 1. Система входа с ограничением попыток
# Запроси у пользователя логин и пароль.
# У пользователя есть 3 попытки для ввода правильных данных.
# Если неверный ввод трижды, вывести "Доступ заблокирован".

# log = "nuri"
# pas = 2424
#
# login1 = input("Enter login:")
# password = input("Enter password:")
# if login1 == log and pas == pas:
#     print("Доступ разрешен")
# else:
#     print("Неправильный логин или пароль. Осталось попыток: 2")
#     login2 = input("Enter login:")
#     password = input("Enter password:")
#     if login2 == log and pas == pas:
#         print("Доступ разрешен")
#     else:
#         print("Неправильный логин или пароль. Осталось попыток: 1")
#         login3 = input("Enter login:")
#         password3 = input("Enter password:")
#         if login3 == log and pas == pas:
#             print("Доступ разрешен")
#         else:
#             print("Неправильный логин или пароль. Осталось попыток: 0. Доступ запрещен.")

# 2. Разрешение на въезд в страну
# Человек может въехать, если у него есть виза или гражданство, и срок действия паспорта не истек.
# Запроси есть_виза (bool), гражданство (bool), паспорт_действителен (bool).
# Выведи "Разрешен въезд" или "Въезд запрещен".

# visa = input("У вас имеется виза? (Впишите Да/Нет)")
# nationality = input("У вас гражданство Терабитии? (Впишите Да/Нет)")
# passport = input("Срок истечения срока паспорта больше чем 6 месяцев? (Впишите Да/Нет)")
#
# if (visa == "Да" or nationality == "Да") and passport == "Да":
#     print("Въезд разрешен")
# else:
#     print("Въезд запрещен")


# 3. Определение високосного года
# Запроси у пользователя год.
# Год високосный, если делится на 4, но не делится на 100, или делится на 400.
# Выведи "Високосный" или "Обычный".

# year = input("Введите год: ")
# if (int(year) % 4 == 0 and int(year) % 100 != 0) or int(year) % 400 == 0:
#     print("Високосный")
# else:
#     print("Обычный")


# 4. Проверка корректности пароля
# Запроси пароль у пользователя.
# Он должен быть не короче 8 символов и содержать хотя бы одну цифру.
# Выведи "Пароль надежный" или "Пароль слабый".

# password = input("Введите пароль: ")
# if len(password) >= 8 and password.isalnum():
#     print("Пароль надежный")
# else:
#     print("Пароль слабый")


# 5. Определение температуры воды
# Запроси температуру воды.
# Выведи "Лед", если <= 0, "Жидкость", если 1–99, "Пар", если >= 100.

# temp = input("Температура воды: ")
# if int(temp) <= 0:
#     print("Лед")
# elif 1 <= int(temp) <= 99:
#     print("Жидкость")
# elif int(temp) >= 100:
#     print("Пар")


# 6. Калькулятор налогов
# Запроси доход.
# Если <= 10 000 – налог 5%, от 10 001 до 50 000 – 10%, больше 50 000 – 20%.
# Выведи сумму налога.

# income = input("Введите сумму вашего дохода: ")
# if int(income) <= 10000:
#     print("Сумма налога (5%)", int(income) * 0.05)
# elif 10001 <= int(income) <= 50000:
#     print("Сумма налога (10%)", int(income) * 0.1)
# elif int(income) >= 50000:
#     print("Сумма налога (20%)", int(income) * 0.2)


# 7. Игра "Камень, ножницы, бумага"
# Пользователь и компьютер вводят "камень", "ножницы" или "бумага".
# Определи победителя по стандартным правилам.

# human = input("Человек, Введите камень, ножницы или бумага: ")
# comp =  input("Комп, Введите камень, ножницы или бумага: ")
# if human == "камень" and comp == "ножницы":
#     print("Человек выиграл")
# if human == "ножницы" and comp == "бумага":
#     print("Человек выиграл")
# if human == "бумага" and comp == "камень":
#     print("Человек выиграл")
# if comp == "камень" and human == "ножницы":
#     print("Комп выиграл")
# if comp == "ножницы" and human == "бумага":
#     print("Комп выиграл")
# if comp == "бумага" and human == "камень":
#     print("Комп выиграл")
# if human == "камень" and comp == "камень":
#     print("Ничья")
# if human == "бумага" and comp == "бумага":
#     print("Ничья")
# if human == "ножницы" and comp == "ножницы":
#     print("Ничья")

#2verison




# 8. Проверка суммы цифр числа
# Запроси у пользователя число.
# Если сумма его цифр четная, выведи "Сумма четная", иначе "Сумма нечетная".

# number = input("Введите четырехзначное число: ")
# if (int(number[0]) + int(number[1]) + int(number [2]) + int(number[3])) % 2 == 0:
#     print("Sum is even")
# else:
#     print("Sum is odd")

# 9. Парковка для электромобилей
# Запроси у пользователя тип машины ("электро" или "бензин").
# Если "электро" – парковка бесплатна, иначе 100 рублей.

# car = input("Введите тип своей машины - электро или бензин: ")
# if car == "электро":
#     print("Парковка бесплатная")
# elif car == "бензин":
#     print("Оплата 100 рублей")


# 10. Кратность чисел
# Запроси два числа a и b.
# Выведи "a кратно b", если a % b == 0, иначе "a не кратно b".

# a = int(input("Введите первое число: "))
# b = int(input("Введите второе число: "))
# if a % b == 0:
#     print("a кратно b")
# else:
#     print("a не кратно b")



# 11. Проверка на счастливый билет
# Запроси шестизначное число.
# Если сумма первых трех цифр равна сумме последних трех – "Счастливый билет!".

# num = input("Введи шестизначное число")
# if int(num[0]) + int(num[1]) + int(num[2]) == int(num[3]) + int(num[4]) + int(num[5]):
#     print("Счастливый билет!")
# else:
#     print("Несчастливый билет")

# 12. Время года по номеру месяца
# Запроси номер месяца (1-12).
# Используя тернарный оператор, определи и выведи время года.

# month = int(input("Enter a number of the month: "))
# print("winter" if int(month) == 1 else "winter" if int(month) == 2 else "winter" if int(month) == 12 else "spring" if int(month) == 3 else "spring" if int(month) == 4 else "spring" if int(month) == 5 else "summer" if int(month) == 6 else "summer" if int(month) == 7 else "summer" if int(month) == 8 else "fall")

# 13. Определение знака числа
# Запроси число.
# Используя тернарный оператор, выведи "+", "-" или "0".

# num = int(input("Enter a number: "))
# print("+" if num > 0 else ("-" if num < 0 else "0"))

# 14. Минимальное из трех чисел
# Запроси три числа.
# Используя тернарный оператор, найди минимальное.

# num1 = int(input("Enter first number"))
# num2 = int(input("Enter second number"))
# num3 = int(input("Enter third number"))
# print(f"Минимальное число {num1}" if int(num1) < int(num2) and  int(num1) < int(num3) else (f"Минимальное число: {num2}" if int(num2) < int(num3)  and int(num2) < int(num1) else f"Минимальное число: {num3}"))

# 15. Оценка успеваемости
# Запроси у пользователя его средний балл (0–100).
# Выведи "Отлично" (>= 85), "Хорошо" (70-84), "Удовлетворительно" (50-69), "Неудовлетворительно" (< 50).

# num = input("Введите ваш средний балл:")
# print("Отлично" if int(num) >= 85 else "Хорошо" if 70 >= int(num) >= 84 else "Удовлетворительно" if 50 >= int(num) >= 69 else "Неудовлетворительно")

# 16. Выбор места в театре
# Запроси у пользователя ряд и место.
# Если ряд <= 3 – "VIP-зона", если 4-10 – "Средний сектор", иначе "Бюджетная зона".

# row = input("Your row number: ")
# seat = input("Your seat number: ")
# print("VIP-zone" if int(row) <= 3 else "Middle sector" if 4 <= int(row) <= 10 else "Budget section5")

# 17. Определение дня недели
# Запроси число от 1 до 7.
# Выведи соответствующий день (1 – Понедельник, ..., 7 – Воскресенье).

# num = input("Enter number between 1-7: ")
# print("Monday" if int(num) == 1 else "Tuesday" if int(num) == 2 else "Wednesday" if int(num) == 3 else "Thursday" if int(num) == 4 else "Friday" if int(num) == 5 else "Saturday" if int(num) == 6 else "Sunday")

# 18. Подсчет цифр числа
# Запроси число.
# Выведи количество его цифр.

# num = input("Enter a number: ")
# print(len(num))

# 19. Сортировка трех чисел
# Запроси три числа.
# Выведи их в порядке возрастания.

# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# num3 = input("Enter third number: ")
# print((num1, num2, num3) if int(num1) < int(num2) < int(num3) else (num1, num3, num2) if int(num1) < int(num3) < int(num2) else (num2, num1, num3) if int(num2) < int(num1) < int(num3) else (num2, num3, num1) if int(num2) < int(num3) < int(num1) else (num3, num1, num2) if int(num3) < int(num1) < int(num2) else (num3, num2, num1))

# 20. Проверка доступа по возрасту
# Запроси возраст пользователя.
# Если возраст меньше 18, вывести "Доступ запрещен", иначе "Доступ разрешен".

# age = input("Enter your age: ")
# print("Access denied" if int(age) < 18 else "Access granted")