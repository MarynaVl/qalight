class MyOwnException(Exception):
    pass


def my_func_with_exception(a: int):
    if not type(a) is int:
        raise MyOwnException(f'має бути число, а не: {type(a)}')


try:
    my_func_with_exception('5')
except Exception as e:
    print(e.__class__)
    print(e)

class ValueShouldBeFromOneToFiveException(Exception):
    pass


def func_(a: int):
    if a not in range(0, 5+1):
        raise ValueShouldBeFromOneToFiveException


try:
    func_(5)
except ValueShouldBeFromOneToFiveException as e:
    print(e)
else:
    print("No exception raise")
finally:
    print('А я тут, як тут, завжди щось виконую')

