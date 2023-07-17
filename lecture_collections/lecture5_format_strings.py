sentense1 = "я {} люблю Україну{}"

print(sentense1.format('дуже', '!'))


# по ключ-значенні
sentense2 = "я {how} {what} Україну"

print(sentense2.format(what='люблю', how='дуже'))


# ще варіант
sentense3 = "я %s Україну"

print(sentense3 % 'дуже люблю')

sentense4 = "я %s %s Україну"

print(sentense4 % ('дуже', 'люблю'))


# форматування f-стрінгами
name = 'Vasya'
lastname = "Bodian"

my_str = f'My favorite friend is {name} {lastname}'
print(my_str)
