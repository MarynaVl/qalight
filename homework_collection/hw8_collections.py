"""
    LIST
    a) Створіть пустий список і додайте до нього 3 різних числа. Виведіть список на екран.
    б) Змініть значення другого елемента в списку. Виведіть оновлений список.
    в) Видаліть третій елемент зі списку. Виведіть оновлений список.
    г) Створіть другий список, з кількома числами більшими за 10. Додайте в кінець першого списку.
    Виведіть на екран зріз списку від третього до п'ятого елементу.
    д) Поміняйте місцями найбільше та найменше число в списку.
"""

list1: list = []
for i in range(3):
    list1.append(i)
print(list1)

list1[1] = 5
print(list1)

del list[2]
print(list1)

list2: list = [2, 11, 3, 13, 4, 33]
list1 += list2
print(list1[2:5])

print(list1)
max_index = list1.index(max(list1))
min_index = list1.index(min(list1))
list1[min_index], list1[max_index] = list1[max_index], list1[min_index]
print(list1)


"""
    TUPLE
    а) Створіть кортеж з трьох різних елементів. Виведіть кортеж на екран.
    Спробуйте змінити значення першого елемента кортежу.
    Спостереження: кортежі є незмінними, тому ця спроба має завершитися помилкою.
    б) Створіть другий кортеж та об'єднайте два кортежі в один. Виведіть оновлений кортеж.
"""

tuple1: tuple = (1, 3, 5)
print(tuple1)

try:
    tuple1[0] = 8
except TypeError:
    print('Кортежі є незмінними. Операція зміни значення елементів кортежу неможлива.')

tuple2: tuple = (4, 2, 8)
print(tuple1 + tuple2)


"""
    SET
    а) Створіть множину, яка містить 4 різних значення. Виведіть множину на екран.
    б) Додайте нове значення до множини. Виведіть оновлену множину.
    в) Видаліть одне значення з множини. Виведіть оновлену множину.
"""

set1: set = {'cat', 'dog', 'mouse', 'horse'}
print(set1)

set1.add('rabbit')
print(set1)

set1.pop()  # так як не вказано інше, видалимо перший елемент з множини
print(set1)


"""
    FROZENSET
    а) Створіть frozenset, що містить 3 різних значення. Виведіть frozenset на екран.
    б) Спробуйте змінити (додати або видалити) значення в frozenset.
    Спостереження: frozenset є незмінним, тому будь-яка спроба зміни має завершитися помилкою.
    в) Створіть ще один frozenset з різними значеннями. Об'єднайте два frozenset в новий frozenset.
    Виведіть отриманий frozenset.
"""

frozenset1: frozenset = frozenset({'meatball1', 'meatball2', 'meatball3'})
print(frozenset1)

try:
    frozenset1.add(4)
except AttributeError:
    print('frozenset є незмінним. Операція додавання/видалення неможлива.')

frozenset2: frozenset = frozenset({'fly1', 'fly2', 'fly3', 'fly4'})
frozenset_union = frozenset1.union(frozenset2)
print(frozenset_union)


"""
    STRING
    а) Створіть рядок, що містить ваше ім'я з маленької літери. Виведіть рядок на екран.
    б) Змініть першу літеру вашого імені на велику літеру. Виведіть оновлений рядок.
    в) Підрахуйте кількість символів у вашому рядку. Виведіть результат.
"""

my_name: str = 'maryna'
print(my_name)

my_name = my_name.capitalize()
print(my_name)

print(len(my_name))


"""
    DICTIONARY
    а) Створіть словник, що містить пари ключ-значення про ваші улюблені продукти (наприклад: ягода -- суниця). 
    Виведіть словник на екран.
    б) Додайте нову пару ключ-значення до словника. Виведіть оновлений словник.
    в) Видаліть одну пару ключ-значення зі словника. Виведіть оновлений словник.
"""

dictionary1: dict = {'berry': 'raspberry', 'vegetable': 'potato', 'fish': 'herring'}
print(dictionary1)

dictionary1.update({'fruit': 'banana'})
print(dictionary1)

dictionary1.pop('berry')
print(dictionary1)
