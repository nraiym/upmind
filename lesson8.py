# 1. Что такое словарь в Python?
#    - Словарь — это структура данных, которая хранит пары "ключ: значение".
#    - Ключи уникальны и неизменяемы.
#    - Значения могут быть любыми типами данных.

# 2. Создание словаря:
#    - Пустой словарь: my_dict = {}
#    - Заполненный словарь: 
#      student = {
#          "name": "Алексей",
#          "age": 21,
#          "city": "Москва"
#      }

# 3. Обращение к значениям по ключу:
#    print(student["name"])  # Алексей

# 4. Методы словарей:
#    - .get(key[, default]) — безопасное получение значения.
#    - .keys() — возвращает все ключи словаря.
#    - .values() — возвращает все значения.
#    - .items() — возвращает пары (ключ, значение).
#    - .update() — обновляет словарь.
#    - .pop(key[, default]) — удаляет ключ и возвращает его значение.
#    - .clear() — очищает словарь.

# 5. Добавление и изменение элементов:
#    student["age"] = 22  # Изменение значения
#    student["grade"] = "A"  # Добавление новой пары

# 6. Удаление элементов:
#    student.pop("city")  # Удаляет пару с ключом 'city'
#    del student["name"]  # Удаляет ключ 'name'

# 7. Проверка наличия ключа:
#    if "name" in student:
#        print("Ключ 'name' есть в словаре!")


# Ознакомительные задачи:
# 1. Создай словарь, содержащий информацию о книге (название, автор, год издания). Выведи автора книги.

book = {
    "Name": "November 9",
    "Author": "Coleen Hoover",
    "Year": 2015,
}
print(book["Author"])

# 2. Создай пустой словарь и добавь в него три ключа: имя, возраст, город.

student = dict()
student["name"] = "Nuraiym"
student["age"] = 23
student["city"] = "Bishkek"
print(student)

# 3. Удали ключ "город" из словаря и выведи результат.
student.pop("city")
print(student)

# 4. Проверь, есть ли ключ "телефон" в словаре и выведи сообщение об этом.

print(student.get("phone", "Такого ключа нет"))

# 5. Измени значение ключа "возраст" на 30.

student["age"] = 30
print(student)

# 6. Создай словарь с именами друзей и их любимыми цветами. Выведи любимый цвет одного из друзей.

friends = {
    "Sophie": "blue",
    "Anna": "white",
    "Kate": "black"
}
print(friends["Anna"])

# 7. Создай словарь студентов и их оценок. Выведи всех студентов и их оценки.

grades = {
    "Anna": "A",
    "Benny": "B",
    "Cole": "F"
}
print(grades.items())

# 8. Используя .get(), получи значение несуществующего ключа с выводом "Нет такого ключа".

print(grades.get("Derek", "НЕТ ТАКОГО КЛЮЧА!"))

# 9. Создай словарь с продуктами и их ценами. Добавь новый продукт и выведи обновленный словарь.
groceries = {
    "Cabbage": 200,
    "Milk": 100,
    "Bread": 25
}
groceries["Carrot"] = 59
print(groceries)

# 10. Подсчитай количество ключей в словаре.
print(len(groceries))

# 11. Создай словарь с номерами автомобилей и их владельцами. Выведи владельца одного из автомобилей.

cars = {
    "456AFK": "Denis",
    "123KG": "Cody",
    "888BMW": "Kyle"
}
print(cars["456AFK"])

# 12. Добавь нового владельца и автомобиль в словарь.
cars["345AA"] = "Mike"
print(cars)

# 13. Удали информацию о владельце автомобиля по номеру.

cars.pop("888BMW")
print(cars)

# 14. Используй метод .items() для вывода всех пар "ключ: значение".

print(cars.items())

# 15. Используй метод .values() для получения всех значений словаря.

print(cars.values())

# 16. Создай словарь с названиями стран и их столицами. Выведи столицу указанной страны.

capitals = {
    "Kyrgyzstan": "Bishkek",
    "Indonesia": "Jakarta",
    "Malaysia": "Kuala Lumpur"
}
print(capitals["Malaysia"])


# 17. Измени название столицы одной из стран.

capitals["Kyrgyzstan"] = "Osh"
print(capitals)

# 18. Проверь наличие страны в словаре перед получением её столицы.

if "Indonesia" in capitals:
    print(capitals["Indonesia"])

# 19. Используй метод .update() для объединения двух словарей.

cars.update(capitals)
print(cars)

# 20. Создай словарь с логинами и паролями пользователей. Проверь правильность пароля для заданного логина.

# users = {
#     "john": "j23950",
#     "sara": "2343ds",
#     "clara": "whatf34"
# }
#
# login = input("Enter login: ")
# password = input("Enter password: ")
#
# if login in users:
#     if users[login] == password:
#         print("Access granted")
#     else:
#         print("Password is not correct")
# else:
#     print("Login and/or password are not correct")

# 21. Создай словарь с днями недели и их порядковыми номерами. Выведи номер среды.

days = {
    "monday": 1,
    "tuesday": 2,
    "wednesday": 3,
    "thursday": 4,
    "friday": 5,
    "saturday": 6,
    "sunday": 7
}

print(days["wednesday"])

# 22. Проверь, есть ли в словаре ключ "воскресенье".

if "sunday" in days:
    print(True)
else:
    print(False)

# 23. Создай словарь с курсами валют и их значениями. Получи значение курса доллара.

currency = {
    "USD": 16555,
    "AUD": 10397,
    "GBP": 21374
}

print(currency["USD"])

# 24. Добавь новую валюту и её курс.

currency["KGS"] = 190.40
print(currency)

# 25. Создай словарь с любимыми фильмами друзей. Выведи фильмы одного из друзей.

movies = {
    "hanna": "avatar",
    "benny": "murder",
    "billie": "hit"
}

print(movies["hanna"])

# 26. Измени фильм в словаре для одного из друзей.

movies["billie"] = "scream"
print(movies)

# 27. Создай словарь с наименованиями товаров и их количеством. Уменьши количество одного из товаров.

products = {
    "whiskey": 34,
    "wine": 250,
    "beer":562
}

products["wine"] = products["wine"] -34
print(products)


# 28. Используй метод .clear() для очистки словаря.

products.clear()
print(products)

# 29. Создай словарь с именами сотрудников и их должностями. Выведи должность указанного сотрудника.

staff = {
    "mike": "marketer",
    "damon": "developer",
    "brad": "babysitter"
}

print(staff["brad"])

# 30. Удали информацию о сотруднике по имени.

staff["mike"] = ""
print(staff)

# 31. Создай словарь с предметами и их баллами. Посчитай общую сумму баллов.

subjects = {
    "geography": 30,
    "chemistry": 25,
    "math": 40,
    "english": 50
}

print(int(subjects["geography"]) + int(subjects["chemistry"]) + int(subjects["math"]) + int(subjects["english"]))

# 32. Создай словарь с животными и их звуками. Выведи звук указанного животного.

pets = {
    "cat": "meow",
    "dog": "woof",
    "frog": "ribbit"
}

print(pets["cat"])


# 33. Измени звук одного из животных.

pets["frog"] = "kwak"
print(pets)

# 34. Создай словарь с товарами и их ценами. Увеличь цену одного из товаров на 10%.

items = {
    "pen": 100,
    "book": 450,
    "stickerpack": 75

}

items["book"] = int(items["book"] + (items["book"] * 0.1))
print(items)

# 35. Создай словарь с именами студентов и их возрастом. Выведи возраст студента с заданным именем.

student = {
    "gwenn": 22,
    "sabrina": 25,
    "clara": 23
}

print(student["sabrina"])

# 36. Проверь наличие студента в словаре перед выводом его возраста.

if "clara" in student:
    print(student["clara"])

# 37. Создай словарь с названиями городов и численностью населения.
# Увеличь численность одного из городов.

cities = {
    "bishkek": 1138000,
    "jakarta": 10670000,
    "new york": 8258000
}

cities["bishkek"] = int(cities["bishkek"]) + 59235
print(cities)

# 38. Используй метод .pop() для удаления ключа и получения его значения.

bye = cities.pop("new york")
print(bye)
print(cities)

# 39. Создай словарь с играми и их рейтингами. Выведи игру с наивысшим рейтингом.

games = {
    "mobile legends": 4.81,
    "counter strike": 4.94,
    "dota": 4.39
}

if games["mobile legends"] > games["counter strike"] and games["mobile legends"] > games["dota"]:
    print("mobile legends", games["mobile legends"])
elif  games["counter strike"] > games["mobile legends"] and games["counter strike"] > games["dota"]:
    print("counter strike", games["counter strike"])
elif games["dota"] > games["counter strike"] and games["dota"] > games["mobile legends"]:
    print("dota", games["dota"])

# 40. Создай словарь с контактами и их телефонами. Выведи телефон указанного контакта.

contacts = {
    "anna": 996555666333,
    "peter": 99645289632,
    "gregory": 465963214569
}

print(contacts["anna"])