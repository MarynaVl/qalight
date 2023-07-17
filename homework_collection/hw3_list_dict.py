# Створити список з 7 елементів типу int, деякі елементи повторююьтся
list_a: list = [1, 2, 3, 5, 1, 2, 3]

# Створити словник з 3 елементів: (ключі типу str: зарплата, бонус, премія) і відповідно значення: 100, 25, 50
dict_b: dict = {'salary': 100, 'bonus': 25, 'premium': 50}


# Список УНІКАЛЬНИХ елементів списку (a)
def unique_number(any_list: list) -> list:
    unique_list = []
    for i in any_list:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list


# Список значень словника (б)
def dict_list(any_dict: dict) -> list:
    my_dict_list = []
    for i in any_dict.values():
        my_dict_list.append(i)
    return my_dict_list


# Перевизначити значення ключа в словнику
def another_salary(value1: int, value2: int):
    new_salary = value1 + value2
    print(new_salary)


# Вивести суму усіх елементів списку (a)
print(sum(list_a))

# Вивести суму усіх УНІКАЛЬНИХ елементів списку (a)
print(sum(unique_number(list_a)))

# Надрукувати суму елемента 3 зі списку (а), та зарплати зі словника (б)
print(int(list_a[2]) + int(dict_b['salary']))

# Надрукувати повну суму доходу на основі словника (б)
print(sum(dict_list(dict_b)))

# Перевизначити зарплату в словнику, збільшивши її на суму премії та надрукувати результат
another_salary(dict_b['salary'], dict_b['premium'])
