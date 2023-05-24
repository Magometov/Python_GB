'''
    Дополнить телефонный справочник возможностью изменения и удаления данных. Пользователь также может ввести фамилию, 
    и Вы должны реализовать функционал для изменения и удаления данных
'''

def telephone_directory():
    getting_started = input("Введите цифру (1 - добавление контакта; 2 - вывод всех; 3 - поиск по фамилии; 4 - изменить данные; 5 - выход) : ")
    match getting_started:
        case ('1'):
            print(user_add())
            return "Добавлено!"
        case ('2'):
            show_all()
            return telephone_directory()
        case ('3'):
            print(search_by_second_name())
        case ('4'):
            change_data()
        case('5'):
            return "Всего доброго!"
        case _:
            print('Ошибка!')
            return telephone_directory()
        

def user_add():
    first_name = input('Введите имя: ')
    second_name = input('Введите фамилию: ')
    patronymic = input('Введите отчество: ')
    number = input('Введите номер: ')

    with open('Lesson 8 - working with files/test.txt', 'a') as data:
        data.write(f"{first_name} {second_name} {patronymic} {number}\n")
        data.close
        return "Запись успешно создана!"
        

def show_all():
    with open('Lesson 8 - working with files/test.txt', 'r') as data:
        print(data.read())
        data.close
    

def search_by_second_name():
    second_name = input("Введите данные: ")

    with open('Lesson 8 - working with files/test.txt') as file:
        lines = file.readlines()
        for line in lines:
            if second_name in line:
                return line


            
def change_data():
        with open('Lesson 8 - working with files/test.txt') as file:
            lines = file.readlines()

        some_data = input("Введите некоторые данные о записи(имя или фамилие): ")
        for line in lines:
            if some_data in line:
                print(line)

        with open('Lesson 8 - working with files/test.txt', 'w') as file:
            for i in lines:
                if some_data not in i:
                    file.writelines(i)
        user_add()


print(telephone_directory())