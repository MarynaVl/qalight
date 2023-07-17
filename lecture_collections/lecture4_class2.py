from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def eat(self):
        pass

    @abstractmethod
    def sleep(self):
        pass


class Mammals(Animal):

    name = 'Mammal'
    voice = 'some voice'

    def eat(self):
        print('I like that meal')

    def sleep(self):
        print('Hrrrrr!')


class Dog(Mammals):

    def __init__(self, name=None, voice=None):  # name та voice необовязкові
        if name:
            self.name = name
        if voice:
            self.voice = voice


dog_1 = Dog
print(dog_1.name, dog_1.voice)  # print видасть Mammal, бо по наслідуванню дані візьме з Mammals

dog_1_1 = Dog()
print(dog_1.name, dog_1_1.voice)  # print видасть Mammal, бо по наслідуванню дані візьме з Mammals

dog_2 = Dog('Bobik')
print(dog_2.name, dog_2.voice)  # print видасть знову Mammal, бо виконається init

dog_3 = Dog('Bobik', 'woof')
print(dog_3.name, dog_3.voice)  # print видасть Bobik та woof
