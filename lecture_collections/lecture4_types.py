# Викликаємо помилку та її оформляємо для друку
def print_data(data: str) -> None:
    if type(data) is str:
        print(data)
    else:
        raise TypeError(f'Incorrect data type {type(data)}, should be string')


print_data('Fgkjhkj kljkjh jhgjhg')
print_data(12)  # Має викликати помилку
