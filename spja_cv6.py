class Animal:
    def __init__(self,name):
        self.name=name

    def sound(self):
        raise NotImplemented()

    def __str__(self):
        return str(self.__class__.__name__)


class Cow:
    def __init__(self, name):
        self.name=name

    def sound(self):
        print("bool")

class Cat:
    def __init__(self, name):
        self.name=name

    def sound(self):
        print("mnau")

class Rabbit:
    def __init__(self,name):
        self.name=name

    def sound(self):
        print("wasup")

class Farm():
    def __init__(self):
        self.animals = []
        self.dict_animals = {}

    def add_animal(self,animal):
        # if not issubclass(animal.__class__, Animal):
        #     raise Exception("{0} is not child of Animal".format(animal.__class__))
        # else:
        self.animals.append(animal)
        self.dict_animals.update({animal.name : animal})

    def write_animals(self):
        for i in self.animals:
            print(i.name)

    def find_animal(self,animal_name):
        return self.dict_animals[animal_name]






