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
    ('Помилки не виникло, все погано')
finally:
    print('Перевірку закінчено')
