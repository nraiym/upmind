# # Список (list) - это упорядоченная изменяемая коллекция элементов.
# from traceback import print_tb
#
# # Пример списка
# fruits = ["яблоко", "банан", "апельсин"]
# print(fruits[0]) # яблоко
#
# # Списки могут содержать разные типы данных
# mixed_list = [42, "hello", 3.14, [1, 2, 3]]
# print (mixed_list[3][1]) # Доступ ко второму элементу вложенного списка →
# print (mixed_list[3][0])
# print (mixed_list[1], mixed_list[0], mixed_list[3][2])
#
# print(mixed_list[-1]) # [1, 2, 3] с конца начинается с -1
#
# # editing index
# hello_world = "hello world"
# print(mixed_list[1])
# mixed_list[1] = hello_world
# mixed_list[2] = 33.11
# print(mixed_list)
#
# print(len(mixed_list))
#
# concatenated_list = mixed_list + fruits
# print(mixed_list + fruits)
# print(len(mixed_list + fruits))
#
# print(fruits * 2)
# ones = ([1] * 10)
# print([1] * 10)
#
# print(fruits)
# print("апельсин" in fruits)
# print("banana" in fruits)
# print("апельсин" in mixed_list)
#
# # 4. Методы списков
# # - append(), insert() - добавление элементов
# # - remove(), pop() - удаление элементов
# # - index(), count() - поиск элементов
# # - sort(), reverse() - сортировка и разворот
# print(fruits)
# fruits. append ("ананас") #вставляет всегда в конец
# fruits.insert(1, "груша") #принимает 2 аргумента - 1 позиция на которую хотите вставить, 2 - что вы хотите вставить
# print(fruits)
#
# # ananas = fruits.pop()
# # print(mixed_list)
# # mixed_list.pop() #pop - удаляет последний элеемент
# # print(mixed_list)
#
# # mixed_list.remove(42)
# # print(mixed_list)
#
# print(mixed_list.index(33.11))
# print(mixed_list.count(33.11)) #подсчет количества одинаковых индексов
# mixed_list.append(33.11)
# print(mixed_list.count(33.11))
# print(mixed_list)
#
# # numbers = [2, 6, 1, 9, 3, 4, 7]
# # print(numbers)
# # print(sorted(numbers))
# # print(numbers) #no connection between them
# #
# # numbers.sort()
# # print(numbers)
#
#
# numbers = [2, 6, 1, 9, 3, 4, 7]
# numbers.sort()
# print(numbers)
# print(numbers[0:2]) #от какого включительно, до какого не включительно - срезы списков -slices
# print(numbers[2:5])

#Задачи для закрепления й
# 1. Создание и работа со списками
# Создай список с 5 любимыми блюдами и выведи третий элемент.

# menu = ["manty", "lagman", "tom yam", "plov", "shashlyk"]
# print(menu[3])

# 2. Индексация
# Дан список чисел [10, 20, 30, 40, 50].
# Используя индексы, замени 30 на 99 и выведи список.

numbers = [10, 20, 30, 40, 50]
print(numbers[2])
numbers[2] = 99
print(numbers[2])

# 3. Операции со списками
# Создай два списка: ["а", "b", "с"] и [1, 2, 3].
# Объедини их в один и выведи результат.

list1 = ["а", "b", "с"]
list2 = [1, 2, 3]
print(list1 + list2)

# 4. Методы списка
listik = [4, 2, 9, 11]
print(listik)
listik.append(7)
print(listik)
listik.remove(2)
print(listik)
listik.sort()
print(listik)

#5
codes = ["python", "java", "c++", "javascript", "php"]
print(codes[0:3])
codes.reverse()
print(codes)

# 6. Итерация по списку
# Дан список имен ["Аня", "Борис", "Вика"]. Используя for, # выведи приветствие для каждог:
# > Привет, Аня!
# > Привет, Борис!
# > Привет, Вика!

names = ["Аня", "Борис", "Вика"]
print("Привет, ",names[0], "!")
print("Привет, ",names[1], "!")
print("Привет, ",names[2], "!")


#7 Вложенные списки
# Дан список [[1, 2], [3, 4], [5, 6]1.
# Выведи 4, обратившись к элементу по индексу.
listnum = [[1,2], [3,4], [5,6]]
print(listnum[1][1])