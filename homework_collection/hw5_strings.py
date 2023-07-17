"""
Є рядок "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
Завдання:
1. Розбити рядок на список окремих слів;
2. Замінити в кожному слові усі голосні літери іншим символом, наприклад #
3. Бонусне завдання: Відновити рядок зі списку, зі вже заміненими словами.
"""

my_string = "Мені дуже подобається вивчати пайтон! Здається, це найлегша з потужних мов для вивчення"
vowels = ['а', 'o', 'у', 'і', 'и', 'е', 'я', 'ю', 'є', 'ї']
replaced_string = []

# Розбити рядок на список окремих слів
split_string = my_string.split(' ')
print(split_string)


# Замінити в кожному слові усі голосні літери іншим символом, наприклад #
def replaced():
    for word in split_string:
        new_word = ''
        for letter in word:
            if letter.lower() in vowels:
                new_word += letter.replace(letter,'#')
            else:
                new_word += letter
        replaced_string.append(new_word)
    print(replaced_string)

replaced()

# Бонусне завдання: Відновити рядок зі списку, зі вже заміненими словами
print(' '.join(replaced_string))
