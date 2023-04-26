'''
    Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
    (т.е. не меньше заданного минимума и не больше заданного максимума)
    Ввод:  [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
    5
    15
    Вывод: [1, 9, 13, 14, 19]
'''

some_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]

min_number = int(input("Введите минимум: "))
max_number = int(input("Введите максимум: "))

result_list = []

for i in range(len(some_list)):
    if min_number <= some_list[i] <= max_number:
        result_list.append(i)

print(result_list)