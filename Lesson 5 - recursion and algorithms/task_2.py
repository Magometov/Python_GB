'''
    Задача 28: Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
    Из всех арифметических операций допускаются только +1 и -1. Также нельзя использовать циклы.

    *Пример:*

    2 2
        4 
'''

def total(first_num: int, second_num: int):
    if second_num == 0:
        return first_num
    
    return total(first_num + 1, second_num - 1)


print(total(2,2))