'''
    Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. 
    Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
    Каждое число вводится с новой строки.
'''


def arithmetic_progression():
    first_el = int(input("Введите первый элемент: "))
    difference = int(input("Введите разность: "))
    list_len = int(input("Введиет количество элементов: "))

    result_list = []

    for i in range(list_len):
        print(first_el + i * difference, end=' ')


arithmetic_progression()