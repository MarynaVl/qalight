"""
    Робота з try-except-else-finally, перехоплення і обробка помилок.

    1.Створити функцію, що приймає число з консолі (використати фунцію input());
    Функція повинна обробити значення таким чином:
    використовуючи вбудовану функцію int() спробувати конвертувати рядок в число (input() завжди повертає рядок).
    Якщо конвертувати не виходить, то вивести в консоль "Entered not valid data".

    2. Створити функцію, що приймає 2 рядки;
    Якщо хоча б один рядок не виходить конвертувати в число, тоді робимо конкатенацію (з'єднуємо рядки),
    якщо ж обидва значення можна конвертувати в числа, то отримуємо їх суму. Результат друкуємо в консоль.

    3. Створити функцію, що приймає значення з консолі. Якщо значення не можна привести до числа,
    тоді просимо користувача ввести інше значення, доки він не введе число. Згадуємо про цикл while.
    Коли користувач вводить число, дякуємо йому )

    4. Створити власне виключення. Наприклад OnlyEvenError. Створити функцію check_digit(), яка приймає число.
    Якщо число не парне, то породжувати це своє виключення, якщо парне, то повертати його (return)

    5. Створити функцію, що буде приймати число як аргумент і викликАти в тілі функцію check_digit,
    в яку передавати це число.

    Якщо виникає помилка, то перехопити її, та збільшити вхідне число на 1. Інакше, помножити число на 2.
    Результат виводити в консоль.
    Також функція повинна надрукувати в консоль "Я все одно завжди щось друкую".
    Використовувати try-except-else-finally

"""


def number_from_console():
    try:
        my_number = input('Enter a number: ')
        number_int = int(my_number)
    except ValueError:
        print(f'Entered not valid data.')
    else:
        print(f'{number_int} is an integer')
    finally:
        print('Operation is finished')


def two_strings_from_console():
    line1 = input('Enter first line: ')
    line2 = input('Enter second line: ')
    try:
        line1_int = int(line1)
        line2_int = int(line2)
    except ValueError:
        print(line1 + line2)
    else:
        print(line1_int + line2_int)
    finally:
        print('Operation is finished')


def data_from_console():
    while True:
        try:
            my_data = input('Enter a number: : ')
            my_data = int(my_data)
            print(f'{my_data} is an integer. Thank you.')
            break
        except ValueError:
            print("That isn`t s valid number. Try again.")


class OnlyEvenError(Exception):
    """Raised when the input value is not even"""
    pass


def check_digit(digit: int):
    if digit % 2 == 0:
        return digit
    else:
        raise OnlyEvenError(f'The number {digit} is not even')


def check_a_number(number: int):
    try:
        check_digit(number)
    except OnlyEvenError:
        print(number + 1)
    else:
        print(number * 2)
    finally:
        print('Я все одно завжди щось друкую')

