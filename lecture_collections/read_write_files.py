# 'r' відкриття для читання (є значення за замовчуванням)
with open('file.txt', 'r') as file:
    print(file.readlines())


# 'w' відкриття для запису: вміст файлу видаляється, якщо файлу не існує - створ.новий
with open('file.txt', 'w') as file:
    file.write('any')

# 'x' відкриття для запису: вміст файлу видаляється, якщо файлу не існує - інша помилка
with open('file.txt', 'x') as file:
    file.write('any\n')
    file.write('string')

# 'a' відкриття для запису: інформація додається до кінця файлу
with open('file.txt', 'a') as file:
    file.write('a-string')

# 't' відкриття в текстовому режимі (за замовчуванням)
with open('file.txt', 't') as file:
    file.write('1')

