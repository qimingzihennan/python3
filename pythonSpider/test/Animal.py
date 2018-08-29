class Animal(object):
    def run(self):
        print('Animal is running ...')


class Dog(Animal):
    pass


class Cat(Animal):
    pass


class Dog1(Animal):
    def run(self):
        print('Dog1 is running ...')

    def eat(self):
        print('Eating meat ...')


class Cat1(Animal):

    def run(self):
        print('Cat1 is running...')


def run_twice(animal):
    animal.run()
    animal.run()


if __name__ == '__main__':
    # dog = Dog()
    # dog.run()
    # cat = Cat()
    # cat.run()
    #
    # dog1 = Dog1()
    # dog1.run()
    # cat1 = Cat1()
    # cat1.run()

    run_twice(Dog1())
