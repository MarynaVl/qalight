class Human:
    favorite_drink: str = 'beer'

    def __init__(self, age: int):
        self.age: int = age
        if age < 18:
            self.favorite_drink = 'juice'

    def drink(self):
        print(f"{self.__class__.__name__}, age {self.age}, likes to drink {self.favorite_drink}")


class Worker(Human):

    def __init__(self, age: int, salary: int):
        super().__init__(age)
        if salary >= 1000 and age >= 18:
            self.favorite_drink = 'whiskey'


Human(10).drink()  # Output: Human, age 10, likes to drink juice
Human(25).drink()  # Output: Human, age 25, likes to drink beer

Worker(15, 100).drink()  # Output: Worker, age 15, likes to drink juice
Worker(15, 2000).drink()  # Output: Worker, age 15, likes to drink juice
Worker(18, 100).drink()  # Output: Worker, age 18, likes to drink beer
Worker(30, 2000).drink()  # Output: Worker, age 30, likes to drink whiskey
