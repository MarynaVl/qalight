# список
list1: list = [1, 2.2, '3', (2, 3, 3), 6, 1]
print(list1)
my_string = 'Any string value'
my_list3 = list(my_string)
print(my_list3)

s = [sym for sym in range(5)]
print(type(s))
print(s)

# методи списку
lst = []

for i in range(5):
    lst.append(i)

print(lst)

lst2 = [0, 1, 2, 3, 4]
lst3 = []

print(lst2)
print(lst3)

for el in lst2:
    x = lst2.pop(0)
    lst3.append(x)

list2 = list(set(list1))
print(type(list2))
print(list2)

# кортеж
my_tuple = (1, 2, 3, 4, 7)

# словник
dictionary = {'one': 1, 'two': 2, 'three': 3}
print(dictionary['one'])

for pair in dictionary.items():
    print(pair)

for key, value in dictionary.items():
    dictionary[key] = value + 1
print(dictionary)

d1 = dict()
print(d1)

keys = ['one', 'two', 'three']
values = [1, 2, 3]
x = dict(zip(keys, values))
print(x)
x['four'] = 4
print(x)

# якщо немає значення по такому ключу і не потрібна помилка
print(x.get('five'))


# множина
unique = set(list1)

print(type(unique))
print(unique)

lst4 = [1, 2, 3, 4, 5]
lst5 = [5, 4, 3, 2, 1]
print(set(lst4) == set(lst5))

lst6 = [1, 2, 3]
print(5 in lst6)

s1 = {1, 2, 3, 4, 5}
s2 = {6, 7, 8, 9, 0}
print(s1.isdisjoint(s2))
