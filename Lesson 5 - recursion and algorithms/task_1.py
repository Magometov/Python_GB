'''
    Задача 26:  Посчитать факториал (произведение 1 до N) и треугольное число (сумма чисел от 1 до N) 
    для числа N ЧЕРЕЗ РЕКУРСИЮ и без циклов
'''


def factorial(number: int):
    if number == 1:
        return 1
    return factorial(number - 1) * number
        

def triangular_number(number: int):
    if number == 1:
        return 1
    return triangular_number(number - 1) + number


def calling_the_resulting_function():
    number = int(input("Введите число: "))

    return f"Факториал - {factorial(number)}, \nТреугольное число - {triangular_number(number)}"


print(calling_the_resulting_function())
