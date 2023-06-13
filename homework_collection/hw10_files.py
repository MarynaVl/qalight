"""
    Читання файлу:
        Відкрийте файл з текстовим вмістом.
        Прочитайте весь вміст файлу.
        Виведіть зчитаний вміст на екран.

    Запис у файл:
        Створіть новий файл або відкрийте існуючий.
        Запишіть у файл деякий текст.
        Закрийте файл.

    Пошук і заміна:
        Відкрийте файл з текстом.
        Прочитайте весь вміст файлу.
        Знайдіть певне слово або фразу у тексті.
        Замініть знайдену фразу на іншу.
        Запишіть змінений текст назад у файл.

    Лічильник слів:
        Відкрийте файл з текстом.
        Прочитайте весь вміст файлу.
        Порахуйте кількість слів у тексті.
        Виведіть результат на екран.

    Аналіз лог-файлу:
        Відкрийте лог-файл.
        Прочитайте весь вміст файлу.
        Знайдіть певні події або помилки у логах.
        Виведіть знайдені події на екран або запишіть їх у новий файл.

    Копіювання файлу:
        Відкрийте вихідний файл, який потрібно скопіювати.
        Відкрийте цільовий файл, куди буде здійснюватися копіювання.
        Прочитайте вміст вихідного файлу.
        Запишіть зчитаний вміст у цільовий файл.
        Закрийте обидва файли.
"""
import json

# Читання файлу
with open('star_wars_intro.txt', 'r') as file:
    print(file.read())

# Запис у файл
with open('star_wars_intro.txt', 'a') as file:
    file.write('\nAttack of the Clones')

# Пошук і заміна
with open('star_wars_intro.txt', 'r') as file:
    new_data = file.read()
    new_data = new_data.replace('Attack of the Clones', 'The phantom menace')

with open('star_wars_intro.txt', 'w') as file:
    file.write(new_data)

# Лічильник слів
with open('star_wars_intro.txt', 'r') as file:
    text = file.read()
    words = text.split()
    word_count = len(words)
    print(word_count)

# Аналіз лог-файлу
with open('log_file_example.json', 'r') as file:
    data = json.load(file)
    for user_dict in data:
        if not user_dict["success"]:
            print(f'{user_dict["user"]} didn\'t logged in')

# Копіювання файлу
with open('star_wars_intro.txt', 'r') as file1:
    with open('copy_sw_intro.txt', 'w') as file2:
        file2.write(file1.read())
