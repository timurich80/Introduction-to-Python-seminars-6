# Задача 30: Заполните массив элементами арифметической прогрессии. Её первый элемент,
# разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.



n = int(input())
a1 = int(input())
d = int(input())
arr = []

for i in range(n):
    c = a1 + i * d
    arr.append(c)
print(c)




# Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)


# from random import randint
# max_index = int(input('Введите начало диапазона: '))
# min_index = int(input('Введите конец диапазона: '))
# # lo, hi = 3, 8
# array = [randint(1, 10) for _ in range(20)]
# print("Original array:", array)
# indexes = [min_index for max_index, v in enumerate(array) if min_index <= v <= max_index]
# print("Indexes:", indexes)
# result = []
# i = len(indexes)
# while i:
#     i -= 1
#     result.append(array.pop(indexes[i]))
# print("Remaining elements:", array)
# print("Required elements:", result)