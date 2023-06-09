'''
    Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов. 
    Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов, 
    а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

    *Пример:*

    6 -> 1  4  1
    24 -> 4  16  4
    60 -> 10  40  10

'''


def paper_cranes(number: int):
    if number < 6 or not isinstance(number, int):
        return "Не соотвествие условиям задачи. number должно быть int и > 2"
    
    count = number // 6
    return f"{number} -> {count} {count * 4} {count}"

    
print(paper_cranes(24))