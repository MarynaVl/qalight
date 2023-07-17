class Human:
    LASTNAME = 'Vlasenko'

    def __int__(self, name: str, age: int):
        self.name: str = name
        self.age: int = age


print(Human.LASTNAME)

# human1 = Human('Maryna', 30)

# print(human1.age, human1.name)


def voice():
    print('Я видаю звук')


class Animal:
    pass


# об’єкти одного типу мають одні й ті самі способи взаємодії
class Dog(Animal):
    pass


dog1 = Dog()
voice()
