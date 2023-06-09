def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        b = 1
        return a / b
    except Exception as unknown_exception:
        print(unknown_exception)


assert divide(10, 2) == 5


class ExceptionClass:

    def some_func(self):
        # raise NotImplementedError
        pass


ExceptionClass().some_func()


def calculate_anything(a: int):
    """
    This function can accept only integers from 1 to 5
    :return:
    """
    if a in range(0, 5):
        print(a)
    else:
        raise ValueError('You should use only integers from 0 to 5')


# calculate_anything(5)

try:
    1 / 1
except ZeroDivisionError as error:
    print(error.__class__)
    print(error.args)
    pass
else:
    pass
finally:
    # print('Я завжди буду тут щось писати')
    pass


class ValueShouldBeFromOneToFiveException(Exception):
    pass


def func_(a: int):
    if a not in range(0, 5 + 1):
        raise ValueShouldBeFromOneToFiveException


try:
    func_(5)
except ValueShouldBeFromOneToFiveException as e:
    print(e)
else:
    print('No exception is rize')
finally:
    print('А я тут як тут, завжди щось виконую')


class MyOwnException(Exception):
    pass


def my_func_with_exception(a: int):
    if not type(a) is int:
        raise MyOwnException(f'має бути число, а не: {type(a)}')


try:
    my_func_with_exception(5)
except MyOwnException:
    print('MyOwnExceptions successfully raised')

tup = (1, 2, 3)
try:
    tup[0] = 5
except TypeError:
    print('Все добре, помилка виникла')
else:
    print('Помилки не виникло, все погано')
finally:
    print('Перевірку закінчено')
