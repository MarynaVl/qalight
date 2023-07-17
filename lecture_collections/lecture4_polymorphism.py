# Поліморфізм
def print_digit(digit: int | float | str):
    if type(digit) in (int, float):
        print(digit)
    elif type(digit) is str:
        try:
            if '.' in digit:
                print(float(digit))
            else:
                print(int(digit))
        except Exception:
            print('Incorrect digit')


print_digit(345)
print_digit(345.55)
print_digit('12')
print_digit('12.444')
