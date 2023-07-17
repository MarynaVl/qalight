# Краще використовувати одинарні лапки
x = 'abcde'

# Екранування лапок
y1 = "My favorite car is 'Nissan'"
y2 = 'Some "text"'

# Перенесення на інший рядок
y3 = "My favorite car is \n 'Nissan'"
print(y3)


# Потрійні рядки для багаторядкового коментаря - для документації
def my_func(my_param):
    """
    :return:
    :param
    :my_param - bla bla bla
    """


# КОНКАТЕНАЦІЯ (додавання)
s1 = 'abc'
s2 = 'def'

print(s1)
print(s2)
print(s1 + s2)

strings_list = ['a', 'b', 'c']

word = ''

for i in strings_list:
    word += i

print(word)

# ДУБЛЮВАННЯ
print(s1 * 3)

# ВИЗНАЧЕННЯ ДОВЖИНИ
a1 = [1, 2, 3, 4]
a2 = 'abcd'
len(a1)
len(a2)


# ЗВЕРНЕННЯ ПО ІНДЕКСУ
text = 'this is my world'

print(text[0])
print(text[2:])
print(text[3:7])
print(text[-2])
print(text[1:-2])
print(text[::-1])


# МЕТОДИ РЯДКІВ
sentence = 'я дуже люблю Україну'

print(sentence.split(' '))

sentence2 = 'я,дуже,люблю,Україну'
print(sentence.split(','))
